from django import forms

class NewDepartamentForm(forms.Form):
    first_name = forms.CharField( max_length=50)
    last_name = forms.CharField( max_length=50)
    departament = forms.CharField( max_length=50)
    short_name = forms.CharField( max_length=20)