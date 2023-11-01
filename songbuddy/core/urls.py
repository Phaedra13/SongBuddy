
from django.urls import path

from . import views
from . import api

app_name = 'core'
urlpatterns = [
    path("", views.index, name="index"),
    path("results/", views.results, name="results"),
    
]