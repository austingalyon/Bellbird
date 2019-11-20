from django import forms

from .models import Chirp

class ChirpForm(forms.ModelForm):
  text = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Enter your chirp"}))

  class Meta:
    model = Chirp
    fields = [ 'text', ]