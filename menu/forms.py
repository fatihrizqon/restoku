from django import forms

class Search(forms.Form):
    name = forms.CharField(max_length=255)