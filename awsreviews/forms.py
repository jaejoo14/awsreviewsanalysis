from django import forms

from .models import Search
from .models import Stream

class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ('query',)

class StreamForm(forms.ModelForm):

    class Meta:
        model = Stream
        fields = ('expr',)
