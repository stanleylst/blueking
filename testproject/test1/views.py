# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    a = request.GET.get('a')
    print a
    return HttpResponse(a)
# Create your views here.
