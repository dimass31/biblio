from django.shortcuts import render
from .models import Book


def landing(request):
    return render(request, 'landing/landing.html', locals())

def home(request):
    books = Book.objects.filter()
    return render(request, 'landing/home.html', locals())
