# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from django.shortcuts import render


def dashboard(request):
    return render(request, 'app/dashboard.html', context={})


def post(request):
    if request.method == 'POST':
        print(request.POST.description)