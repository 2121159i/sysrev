from django import forms
from django.contrib.auth.models import User
from sysrev.models import *

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ResearcherForm(forms.ModelForm):

    forename    = forms.CharField(required=True)
    surname     = forms.CharField(required=True)

    class Meta:
        model = Researcher
        fields = ('forename', 'surname')


# Model form for a new review
class ReviewForm(forms.ModelForm):
    title           = forms.CharField(required=True)
    description     = forms.CharField(required=True)
    query_string    = forms.CharField(required=True)

    class Meta:
        model = Review
        fields = ('title', 'description', 'query_string')