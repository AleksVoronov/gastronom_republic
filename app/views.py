"""
Definition of views.
"""

from .forms import ContactForm
# from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpRequest


def hlavní(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/hlavní.html', {'title': 'Gastronom Republic'})


def kontakty(request):
    #"""Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(request, 'app/kontakty.html', {'title': 'Gastronom Republic', })


def o_nás(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/o_nás.html',
        {
            'title': 'Gastronom Republic',

        }
    )


def kontakty(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'app/kontakty.html', {'form': form})
