from django.urls import include, path
from . import views

urlpatterns = [
    path('<month>', views.monthly_challenge),
]