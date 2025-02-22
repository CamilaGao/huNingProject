from django.shortcuts import render

from test import award
from .models import Award


# Create your views here.
def survey(request):
    return render(request, 'survey.html', {
        'active_menu': 'about',
        'sub_menu': 'survey',
    })


def honor(request):
    awards = Award.objects.all()
    return render(request, 'honor.html', {
        'active_menu': 'about',
        'sub_menu': 'honor',
        'awards': awards,
    })
