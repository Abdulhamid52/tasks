from main.models import Work
from django import forms
from django.forms import fields
from accounts.models import *

class WorkerAddForm(forms.ModelForm):

    class Meta:
        model = Workers
        fields = ['name', 'surname']


class WorkAddForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = ['title','salary']