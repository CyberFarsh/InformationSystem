from django import forms
from .models import Initiative


class initiative(forms.ModelForm):
    class Meta:
        model = Initiative
        fields = ["name", "type", "budget"]
