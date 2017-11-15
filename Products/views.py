
from django.shortcuts import render
from .forms import *


def genre(request):
    form = GenreForm(request.POST or None)
    # return render(request, 'hotel/hotel.html', locals())

def customers(request):
    form = CustomersForm(request.POST or None)


def developers(request):
    form = DevelopersForm(request.POST or None)


def images(request):
    form = ImagesForm(request.POST or None)


def games(request):
    form = GamesForm(request.POST or None)    