from django import forms
from projects.models import Project, HelpOffer
from users.models import Skill, Country, State
from django.db.models.fields.files import ImageFieldFile

class ProjectCreationForm(forms.ModelForm):
    
    CHOICES = [(True, 'Yes'),
        (False, 'No')]

    title           = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
                            attrs={'placeholder': 'Title'})) 
    skills          = forms.ModelMultipleChoiceField(
                    queryset=Skill.objects.all().order_by('skill_name'), \
                    widget=forms.SelectMultiple(
                    attrs={'class': 'chzn-select', 'data-placeholder': 'Select Skill',}),
                    required=False)
    description     = forms.CharField(max_length=1000, widget=forms.Textarea(
                            attrs={'placeholder': 'Title'}), required=False)
    image           = forms.ImageField(required=False)
    country         = forms.ModelChoiceField(empty_label="Country...", 
                        queryset=Country.objects.all(), widget=forms.Select(
                        attrs={'class': 'chzn-select change-color', 'data-placeholder': 'Select Country'}))
    state           = forms.ModelChoiceField(empty_label="State...", 
                    queryset=State.objects.all(), widget=forms.Select(
                    attrs={'class': 'chzn-select change-color', 'data-placeholder': 'Select State'}))
    city            = forms.CharField(max_length=30, widget=forms.TextInput(
                            attrs={'placeholder': 'City'}))
    lat             = forms.FloatField(required=True)
    lon             = forms.FloatField(required=True)
    need_locals     = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),
                        required=True)

    def clean_image(self):
        image = self.cleaned_data['image']
        check_no_new_image = isinstance(image, ImageFieldFile)
    
        if image and not check_no_new_image:
            if image._size > 1*1024*1024:
                raise forms.ValidationError("Image file too large ( maximum 1mb )")
            return image

    class Meta:
        model       = Project
        exclude     = ('charity',)
        fields      = ('title', 'description', 'image', 'skills', 
                        'need_locals', 'country',
                        'state', 'city', 'lat', 'lon')

class ProjectChangeForm(ProjectCreationForm):
    
    status          = forms.ChoiceField(choices=Project.STATUS_CHOICES,
                    widget=forms.RadioSelect())

    class Meta:
        model       = Project
        exclude     = ('charity',)
        fields      = ('title', 'description', 'image', 'skills', 
                        'need_locals', 'country',
                        'state', 'city', 'lat', 'lon', 'status')


class HelpOfferForm(forms.ModelForm):
    '''
    Sends a help offer.
    '''
    message = forms.CharField(max_length=500, widget=forms.Textarea, required=False)

    class Meta:
        model   = HelpOffer
        fields  = ('message',)

    def clean(self):
        # These checks should be redundant as the form is not rendered
        # if the conditions aren't met
        # Check if the user is a developer
        profile         = self.view_request.user.get_profile()
        if profile.user_type    != 'Developer':
            raise forms.ValidationError('You must log in as a Developer to offer your help on projects')
       
        project_id              = self.view_request_pk
        project                 = Project.objects.get(id=project_id)
        
        # Check if the user has already offered to help
        has_already_offered =   HelpOffer.objects.filter(sender=profile, project=project)
        if has_already_offered:
            raise forms.ValidationError('You have already offered to help on this project')
        return self.cleaned_data

