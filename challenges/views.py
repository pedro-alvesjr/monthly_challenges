from django.http import HttpResponse, HttpResponseNotFound
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
    else:
        return HttpResponseNotFound('Month not supported.')

    return HttpResponse(challenge_text)
