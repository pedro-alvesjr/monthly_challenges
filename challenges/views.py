from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


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


def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f'<li><a href=\'{month_path}\'>{capitalized_month}</a></li>'

    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month.')
    month_chosen = months[month - 1]

    redirect_path = reverse('month-challenge', args=[month_chosen])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html')
    except:
        HttpResponseNotFound('<h1>Invalid month.</h1>')
