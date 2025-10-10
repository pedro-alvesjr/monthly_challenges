from django.urls import include, path
from . import views

urlpatterns = [
    path('january', views.index),
]