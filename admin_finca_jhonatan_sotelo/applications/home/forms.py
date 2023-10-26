from django import forms

from.models import JhonatanSotelo

class CrearForm(forms.ModelForm):
    
    class Meta:
        model = JhonatanSotelo
        fields=("__all__")