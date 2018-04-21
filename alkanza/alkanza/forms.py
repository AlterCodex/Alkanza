from django import forms

class SearchForm(forms.Form):
    search_address = forms.CharField(max_length=254, help_text='Required. Inform a place.')
    radius = forms.IntegerField(help_text='Required, Radius for search')
    key_word = forms.CharField(max_length=254, help_text='Required. Search Parameter')
