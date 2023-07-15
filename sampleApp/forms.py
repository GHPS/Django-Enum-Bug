from django import forms

from .models import sampleModel

class sampleForms(forms.ModelForm):

    class Meta:
        model=sampleModel
        fields='__all__'

    stTitle=forms.CharField()
    eAsset=forms.ChoiceField(choices=[(dcEntry.value, dcEntry.label) for dcEntry in sampleModel.eAssets])
