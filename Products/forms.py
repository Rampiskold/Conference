
from django import forms

from .models import *


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        exclude = [""]


class DevelopersForm(forms.ModelForm):
    class Meta:
        model = Developers
        exclude = [""]


class CustomersForm(forms.ModelForm):
    class Meta:
        model = Customers
        exclude = [""]


class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        exclude = [""]


class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        exclude = [""]

