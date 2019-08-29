from django import forms

from .models import Search
from .models import Stream

class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        widgets  = {
             'query' : forms.Textarea(attrs={'rows':4, 'cols':15}),
        }
        fields = ('query',)

class StreamForm(forms.ModelForm):

    class Meta:
        model = Stream
        fields = ('expr',)
