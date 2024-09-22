from django.shortcuts import render, redirect
from .models import Portfolio, About, Service, Resume_work, Resume_education
from .forms import ContactForm


def index(request):
    return render(request, "index.html")


def blog(request):
    return render(request, "blog.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")