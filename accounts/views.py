from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from .forms import *

# Create your views here.

class RegisterView(View):
    
    def get(self, request):
        form = RegisterForm(request.GET)
        context = {
            'form':form
        }
        return render(request, 'register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                u = form.save()
                user = UserProfile.objects.create(
                    user=u,
                    name=u.first_name,
                    surname=u.last_name
                )
                user.save()
                return redirect('/accounts/login/')
        context = {
            'form':form
        }
        return render(request, 'register.html', context)