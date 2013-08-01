from django import forms
from projects.models import Project, Request
from users.models import Skill, Country, State

class ProjectSearchForm(forms.Form):
    
    keywords        = forms.CharField(max_length=100, required=False,
                        widget=forms.TextInput(
                            attrs={'class': 'vol-search'})) 
    skills          = forms.ModelMultipleChoiceField(
                    queryset=Skill.objects.all().order_by('skill_name'), \
                    widget=forms.SelectMultiple(
                    attrs={'class': 'chzn-select', 'data-placeholder': 'Select Skill',}),
                    required=False)
    country         = forms.ModelChoiceField(empty_label="Please select a country", 
                        queryset=Country.objects.all(), required=False, widget=forms.Select(
                        attrs={'class': 'chzn-select', 'data-placeholder': 'Select Country'}))
    state           = forms.ModelChoiceField(empty_label="Please select a state", required=False,
                    queryset=State.objects.all(), widget=forms.Select(
                    attrs={'class': 'chzn-select', 'data-placeholder': 'Select State'}))
    city            = forms.CharField(max_length=100, required=False,
                        widget=forms.TextInput(
                            attrs={'class': 'vol-search'})) 
    lat             = forms.FloatField(required=False)
    lon             = forms.FloatField(required=False)

    class Meta:
        fields = ('keywords', 'skills', 'country', 'state', 'city', 'lat', 'lon')