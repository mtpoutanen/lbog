from django import forms
from projects.models import Project, Request
from users.models import Skill, Country, State

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
    description     = forms.CharField(widget=forms.Textarea(
                            attrs={'placeholder': 'Title'}), required=False)
    logo            = forms.ImageField(required=False)
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

    # def save(self, commit=False):
    #     project = Project.objects.create()
    #     return project        
        

    #     return project

class RequestForm(forms.ModelForm):

    message         = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model       = Request
        fields      = ('message',)
            # 'project')


