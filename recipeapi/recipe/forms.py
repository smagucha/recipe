from django import forms

class searchForm(forms.Form):
    search = forms.CharField( max_length=100)
  
