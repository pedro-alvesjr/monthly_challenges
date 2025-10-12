from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

monthly_challenges = {
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

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    month_chosen = months[month]
    return HttpResponseRedirect('/challenges/' + month_chosen)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        HttpResponseNotFound('Invalid month.')