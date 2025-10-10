from django.urls import include, path
from . import views

urlpatterns = [
    path('january', views.january),
    path('february', views.february)
]