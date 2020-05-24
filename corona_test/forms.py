from django import forms
from .models import *

CHOICES = [('Yes', 'Yes'), ('No', 'No'), ('Not Sure', 'Not Sure')]
COUNTRIES = [('None', 'None'), ('China', 'China'), ('USA', 'USA'), ('Italy', 'Italy'), ('Spain', 'Spain')]

class CoronaForm(forms.Form):
    fever = forms.ChoiceField(widget=forms.RadioSelect(attrs={
        'id' : 'fever'
    }), choices=CHOICES)
    cold = forms.ChoiceField(widget=forms.RadioSelect(attrs={
        'id' : 'cold'
    }), choices=CHOICES)
    fatigue = forms.ChoiceField(widget=forms.RadioSelect(attrs={
        'id' : 'fatigue'
    }), choices=CHOICES)
    cough = forms.ChoiceField(widget=forms.RadioSelect(attrs={
        'id' : 'cough'
    }), choices=CHOICES)
    short_breath = forms.ChoiceField(widget=forms.RadioSelect(attrs={
        'id' : 'short_breath'
    }), choices=CHOICES)
    met_positive_person = forms.ChoiceField(widget=forms.RadioSelect(attrs={
        'id' : 'met_positive_person'
    }), choices=CHOICES)
    countries = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={
        'id' : 'countries'
    }), choices=COUNTRIES)