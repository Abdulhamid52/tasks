from django.shortcuts import render
from django.views.generic import View
from .models import *

# Create your views here.

class HomeView(View):

    def get(self, request):
        return render(request, 'main.html')