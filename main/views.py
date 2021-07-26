from django.shortcuts import redirect, render
from django.views.generic import View
from .models import *
from accounts.models import UserProfile
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(LoginRequiredMixin, View):

    def get(self, request):
        post = Work.objects.filter(user=request.user)
        return render(request, 'main.html',{'post':post})

class AddWorker(LoginRequiredMixin, View):

    def get(self, request):
        user = UserProfile.objects.get(id=request.user.user_pro.id)
        form = WorkerAddForm(request.GET)
        context = {
            'form':form
        }
        return render(request, 'addworker.html', context)

    def post(self, request):
        user = UserProfile.objects.get(id=request.user.user_pro.id)
        form = WorkerAddForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                new = form.save()
                user.workers.add(new)
                user.save()
                return redirect('/')
        else:
            form = WorkerAddForm()
        context = {
            'form':form
        }
        return render(request, 'addworker.html', context)


class AddWork(LoginRequiredMixin, View):

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        form = WorkAddForm(request.GET)
        context = {
            'user':user,
            'form':form
        }
        return render(request, 'addwork.html', context)

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        form = WorkAddForm(request.GET)
        if request.method == 'POST':
            w = request.POST['workers']
            workers = Workers.objects.filter(id=w)
            if form.is_valid():
                new = form.save(commit=False)
                post = Work.objects.create(
                    user=user,
                    title=new.title,
                    salary=new.salary
                )
                post.workers.add(workers)
                post.save()
                return redirect('/')
        else:
            form = WorkAddForm()
        context = {
            'user':user,
            'form':form
        }
        return render(request, 'addwork.html', context)