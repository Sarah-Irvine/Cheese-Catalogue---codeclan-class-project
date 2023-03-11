from django import forms

class CheeseForm(forms.Form):
    name = forms.CharField(max_length=255)
    strength = forms.IntegerField()
    colour = forms.CharField(max_length=255)
    country = forms.CharField(max_length=255)
    age = forms.IntegerField()