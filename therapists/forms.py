from django import forms
from .models import Therapist

class TherapistForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = ['profile', 'qualification', 'experience']