from django.shortcuts import render, HttpResponse #import HttpResponse
from .models import*
# Create your views here.
# file: appName/views.py


def home(request):
  books = Book.objects.all()
  data={
    'books':books
  }
  return render(request, 'home.html',data)

def about(request):
  return render(request, 'about.html')

def contact_us(request):
  return render(request, 'contact.html')

def Custom_Order(request):
  return render(request, 'Custom_Order.html')