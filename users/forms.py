# https://github.com/recreatic/django-custom-user/blob/master/custom_user/forms.py

from django import forms
from django.contrib.auth.models import User
from users.models import UserProfile, Skill, Country, State
from django.db.models.fields.files import ImageFieldFile

class MyBaseForm(forms.ModelForm):
    
    error_messages = {
        'charity_skills': ("A Charity cannot select skills"), #this shouldn't even \
        # be possible because of the UI
        'too_many_skills': ("Please select a maximum of 5 skills"),
        'no_email': ("This field is required"),
        'no_charity': ("You must select a Charity Name"),
        'duplicate_email': ("An account has been registered for that email address"),
        'duplicate_username': ("The username exists already"),
        'password_mismatch': ("The two password fields didn't match."),
        't_and_c': ("Please accept our terms and conditions."),
    }

    # Many of the attributes are set in users/templates/users/users/js/userfx.js
    # Note that the name information is attached to the UserProfile rather
    # than the User for ease of editing later

    given_name      = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
                            attrs={'placeholder': 'First Name...'}))
    family_name     = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
                            attrs={'placeholder': 'Family Name...'}))
    title           = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
                            attrs={'placeholder': 'Title...'})) 
    company_name    = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
                            attrs={'placeholder': 'Organisation Name...'}))
    www             = forms.CharField(max_length=50, required=False, widget=forms.TextInput(
                            attrs={'placeholder': 'www.example.com'}))
    country         = forms.ModelChoiceField(empty_label="Country...", 
                    queryset=Country.objects.all(), widget=forms.Select(
                    attrs={'class': 'chzn-select change-color'}))
    state           = forms.ModelChoiceField(empty_label="State...", 
                    queryset=State.objects.all(), widget=forms.Select(
                    attrs={'class': 'chzn-select change-color'}))
    city            = forms.CharField(max_length=30, widget=forms.TextInput(
                            attrs={'placeholder': 'City...'}))
    # post_code       = forms.CharField(max_length=10, required=False)
    # address         = forms.CharField(max_length=50, required=False)
    lat             = forms.FloatField(required=True)
    lon             = forms.FloatField(required=True)
    description     = forms.CharField(max_length=1000, widget=forms.Textarea(
                            attrs={'placeholder': 'Description...'}), required=False)
    skills          = forms.ModelMultipleChoiceField(
                    queryset=Skill.objects.all().order_by('skill_name'), \
                    widget=forms.SelectMultiple(
                    attrs={'class': 'chzn-select', 'data-placeholder': 'Select Skill',}),
                    required=False)
    logo            = forms.ImageField(required=False)
    allow_contact   = forms.BooleanField(required=False)

    class Meta:
        abstract    = True

    def clean_logo(self):
        image = self.cleaned_data['logo']
        check_no_new_image = isinstance(image, ImageFieldFile)
    
        if image and not check_no_new_image:
            if image._size > 1*1024*1024:
                raise forms.ValidationError("Image file too large ( maximum 1mb )")
            return image


class MyCreationForm(MyBaseForm):
    """
    A form for creating new users. Includes all the required fields, plus a
    repeated password.
    """
    
    CHOICES         = [('Developer', 'Developer'),
                        ('Charity', 'Charity / Non-profit')]
    username        = forms.CharField(max_length=30, required=True)
    email           = forms.EmailField(max_length=100, required=True) 
    password1       = forms.CharField(widget=forms.PasswordInput)
    password2       = forms.CharField(widget=forms.PasswordInput,)
    accept_t_and_c  = forms.BooleanField(required=True)
    user_type       = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),
                    required=True)

    class Meta:
        model       = UserProfile
        exclude     = ('user',)
        fields      = ('user_type', 'username', 'email', 'given_name', 'family_name', 'title', \
        'company_name', 'country', 'state', 'city', 'lat', 'lon', 'description', 'logo', 'allow_contact', 'accept_t_and_c', 'www')
    
    def clean_skills(self):
        skills = self.cleaned_data["skills"]
        user_type = self.cleaned_data["user_type"]
        if user_type == 'Developer' and len(skills) > 5:
            raise forms.ValidationError(self.error_messages['too_many_skills'])
        else:
            if user_type != 'Charity' and skills:
                skills = []
            return skills

    def clean_accept_t_and_c(self):
        if self.cleaned_data['accept_t_and_c'] == False:
            raise forms.ValidationError(
                self.error_messages['t_and_c'])

    def clean_allow_contact(self):
        if self.cleaned_data['user_type'] == 'Charity':
            self.cleaned_data['allow_contact'] = True
        else:
            if not self.cleaned_data['allow_contact']:
                self.cleaned_data['allow_contact'] = False
        return self.cleaned_data['allow_contact']



    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2


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

    def clean_company_name(self):
        company_name    = self.cleaned_data['company_name']
        user_type       = self.cleaned_data['user_type']
        if user_type == 'Charity' and not company_name:
            raise forms.ValidationError(self.error_messages['no_charity'])


    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data.get("username"),
            email=self.cleaned_data["email"],
            )
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class MyChangeForm(MyBaseForm):
    
    def clean_allow_contact(self):
        if not self.cleaned_data['allow_contact']:
            self.cleaned_data['allow_contact'] = False
            # import pdb;
            # pdb.set_trace();
        return self.cleaned_data['allow_contact']

    def clean_skills(self):
        skills = self.cleaned_data["skills"]
        if len(skills) > 5:
            raise forms.ValidationError(self.error_messages['too_many_skills'])
        return skills

    def clean_company_name(self):
        view_request = self.view_request
        user_type = view_request.user.get_profile().user_type
        company_name    = self.cleaned_data['company_name']
        if user_type == 'Charity' and not company_name:
            raise forms.ValidationError(self.error_messages['no_charity'])
        return self.cleaned_data['company_name']

    class Meta:
        model = UserProfile
        exclude     = ('user',)
        fields      = ('given_name', 'family_name', 'title', \
        'company_name', 'country', 'state', 'city', 'lat', 'lon', 'description', 'logo', 'allow_contact', 'www')