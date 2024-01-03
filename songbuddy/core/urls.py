
from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path("core/", views.index, name="index"),
    path("core/results/", views.results, name="results"),
]