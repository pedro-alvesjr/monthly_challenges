from django.urls import include, path
from . import views

urlpatterns = [
    path(''),
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name='month-challenge')
]
