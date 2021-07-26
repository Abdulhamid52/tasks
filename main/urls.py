from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("addworker/", AddWorker.as_view(), name="add_worker"),
    path("addwork/", AddWork.as_view(), name="add_work"),
]
