from django import forms


class initiative(forms.Form):
    name = forms.CharField()
    budget = forms.CharField()
    type = forms.CharField()
