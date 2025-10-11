from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def monthly_challenges(request, month):
    challenge_text = None
    
    if month == 'january':
        challenge_text = 'Eat meat every day.'
    elif month == 'february':
        challenge_text = 'Exercise every morning.'
    elif month == 'march':
        challenge_text = 'Read two books.'

    return HttpResponse(challenge_text)
