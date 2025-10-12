from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

monthly_challenge = {
    'january': 'Eat meat every day.',
    'february': 'Exercise every morning.',
    'march': 'Read two books.',
    'april': 'Eat meat every day.',
    'may': 'Exercise every morning.',
    'june': 'Read two books.',
    'july': 'Eat meat every day.',
    'august': 'Exercise every morning.',
    'september': 'Read two books.',
    'october': 'Eat meat every day.',
    'november': 'Exercise every morning.',
    'december': 'Read two books.',
}

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        return HttpResponse(challenge_text)
    except:
        HttpResponseNotFound('Invalid month.')