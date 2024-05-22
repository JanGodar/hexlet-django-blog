from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse


def article(request):
    return render(request, 'base.html')
# return HttpResponseRedirect(reverse('red', kwargs={'tags': 'python', 'article_id': 42}))


def about(request):
    return render(request, 'about.html')