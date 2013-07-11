# https://github.com/recreatic/django-custom-user/blob/master/custom_user/forms.py

from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
# from django.contrib.admin.forms import AdminAuthenticationForm
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _
# # from emailusernames.utils import user_exists

from users.models import UserProfile, Skill, Country, State

# ERROR_MESSAGE = _("Please enter a correct email and password. ")
# ERROR_MESSAGE_RESTRICTED = _("You do not have permission to access the admin.")
# ERROR_MESSAGE_INACTIVE = _("This account is inactive.")

# class MyAuthenticationForm(AuthenticationForm):
#     """
#     Override the default AuthenticationForm to force email-as-username behavior.
#     """
#     email = forms.EmailField(label=_("Email"), max_length=75)
#     message_incorrect_password = ERROR_MESSAGE
#     message_inactive = ERROR_MESSAGE_INACTIVE

#     def __init__(self, request=None, *args, **kwargs):
#         super(MyAuthenticationForm, self).__init__(request, *args, **kwargs)
#         del self.fields['username']
#         self.fields.keyOrder = ['email', 'password']

#     def clean(self):
#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')

#         if email and password:
#             self.user_cache = authenticate(email=email, password=password)
#             if (self.user_cache is None):
#                 raise forms.ValidationError(self.message_incorrect_password)
#             if not self.user_cache.is_active:
#                 raise forms.ValidationError(self.message_inactive)
#         self.check_for_test_cookie()
#         return self.cleaned_data

class MyBaseForm(forms.ModelForm):
    
    error_messages = {
        'no_skills': ("Please select at least one skill"),
        'charity_skills': ("A Charity cannot select skills"), #this shouldn't even \
        # be possible because of the UI
        'too_many_skills': ("Please select a maximum of 5 skills"),
        'no_email': ("This field is required"),
        'duplicate_email': _("An account has been registered for that email address"),
        'duplicate_username': _("The username exists already"),
        'password_mismatch': _("The two password fields didn't match."),
    }

    CHOICES         = [('Developer', 'Developer'),
                        ('Charity', 'Charity / Non-profit')]
    #note that all the attributes are set in users/templates/users/users/js/userfx.js
    username        = forms.CharField(max_length=30, required=True)
    email           = forms.EmailField(max_length=100, required=True) 
    first_name      = forms.CharField(max_length=30, required=False)
    last_name       = forms.CharField(max_length=30, required=False)
    user_type       = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),
                    required=False)
    title           = forms.CharField(max_length=30, required=False) 
    company_name    = forms.CharField(max_length=30, required=False)
    country         = forms.ModelChoiceField(empty_label="Please select a country", 
                    queryset=Country.objects.all(), widget=forms.Select(
                    attrs={'class': 'chzn-select', 'data-placeholder': 'Select Country'}))
    state           = forms.ModelChoiceField(empty_label="Please select a state", 
                    queryset=State.objects.all(), widget=forms.Select(
                    attrs={'class': 'chzn-select', 'data-placeholder': 'Select State'}))
    city            = forms.CharField(max_length=30)
    post_code       = forms.CharField(max_length=10, required=False)
    address         = forms.CharField(max_length=50, required=False)
    description     = forms.CharField(widget=forms.Textarea, required=False)
    skills          = forms.ModelMultipleChoiceField(
                    queryset=Skill.objects.all().order_by('skill_name'), \
                    widget=forms.SelectMultiple(
                    attrs={'class': 'chzn-select', 'data-placeholder': 'Select Skill',}),
                    required=False)
    logo            = forms.ImageField(required=False)
    password1       = forms.CharField(widget=forms.PasswordInput)
    password2       = forms.CharField(widget=forms.PasswordInput,)

    class Meta:
        model = UserProfile
        exclude = ('user',)
        fields = ('user_type', 'username', 'email', 'first_name', 'last_name', 'title', \
        'company_name', 'country', 'state', 'city', 'post_code', 'address', 'description', 'logo')

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email:
            raise forms.ValidationError(self.error_messages['no_email'])

        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['duplicate_email'])

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def clean_skills(self):
        skills = self.cleaned_data["skills"]
        user_type = self.cleaned_data["user_type"]
        if user_type == 'Developer' and not skills:
            raise forms.ValidationError(self.error_messages['no_skills'])
        elif user_type == 'Developer' and len(skills) > 5:
            raise forms.ValidationError(self.error_messages['too_many_skills'])
        elif user_type != 'Developer' and skills:
            raise forms.ValidationError(self.error_messages['charity_skills'])
        else:
            return skills

class BaseCreationForm(MyBaseForm):
    """
    A form for creating new users. Includes all the required fields, plus a
    repeated password.
    """
    def save(self, commit=True):
        #This line makes it work. When commented, the error appears
        # print self
        ###  
        user = User.objects.create_user(
            username=self.cleaned_data.get("username"),
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            email=self.cleaned_data["email"],
            )
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user




# class MyUserChangeForm(forms.ModelForm):
#     """
#     A form for updating users. Includes all the fields on the user, but
#     replaces the password field with admin's password hash display field.
#     """

#     password = ReadOnlyPasswordHashField(label=_("Password"),
#         help_text=_("Raw passwords are not stored, so there is no way to see "
#                     "this user's password, but you can change the password "
#                     "using <a href=\"password/\">this form</a>."))

#     class Meta:
#         model = MyUser

#     def __init__(self, *args, **kwargs):
#         super(MyUserChangeForm, self).__init__(*args, **kwargs)
#         f = self.fields.get('user_permissions', None)
#         if f is not None:
#             f.queryset = f.queryset.select_related('content_type')

#     def clean_password(self):
#         # Regardless of what the user provides, return the initial value.
#         # This is done here, rather than on the field, because the
#         # field does not have access to the initial value
#         return self.initial["password"]