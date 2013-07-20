from django import forms
from projects.models import Project
from users.models import Skill, Country, State

class ProjectCreationForm(forms.ModelForm):
    
    CHOICES = [(True, 'Yes'),
        (False, 'No')]

    title           = forms.CharField(max_length=30, required=False) 
    skills          = forms.ModelMultipleChoiceField(
                    queryset=Skill.objects.all().order_by('skill_name'), \
                    widget=forms.SelectMultiple(
                    attrs={'class': 'chzn-select', 'data-placeholder': 'Select Skill',}),
                    required=False)
    description     = forms.CharField(widget=forms.Textarea, required=False)
    logo            = forms.ImageField(required=False)
    country         = forms.ModelChoiceField(empty_label="Please select a country", 
                        queryset=Country.objects.all(), widget=forms.Select(
                        attrs={'class': 'chzn-select', 'data-placeholder': 'Select Country'}))
    state           = forms.ModelChoiceField(empty_label="Please select a state", 
                    queryset=State.objects.all(), widget=forms.Select(
                    attrs={'class': 'chzn-select', 'data-placeholder': 'Select State'}))
    city            = forms.CharField(max_length=30)
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

    # def save(self, commit=False):
    #     project = Project.objects.create()
    #     return project        
        

    #     return project

class ProjectChangeForm(forms.ModelForm):

    class Meta:
        model       = Project
        exclude     = ('charity',)
        fields      = ('title', 'description', 'image', 'skills_needed', 
                        'status', 'need_locals', 'country',
                        'state', 'city', 'lat', 'lon')  
