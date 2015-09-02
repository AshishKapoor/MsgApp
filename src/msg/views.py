#!/usr/bin/env python
#**********************************************************************#
# File Name: views.py
# Writen By: Ashish Kapoor
# Project Name: Activity for Zenatix
# Purpose of this file: Definations of all the views.
#**********************************************************************#
from django.contrib import messages
from django.shortcuts import render
from .forms import allMsgsForm, contactForm, msgForm
# Create your views here.
from django.conf import settings
from .models import msg

#Home Funtion Definition
def home (request):
    title = 'Welcome'
    if request.user.is_authenticated():
        title = "%s" %(request.user)

    form = msgForm(request.POST or None)
    context = {
        "title": title,
    }

    return render(request, "home.html", context)

#Contact Function definition
def contact(request):
    title = 'Send Message:'
    form = msgForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Message sent! via MSG App')

    return render(request, "forms.html", context)

#Retreive all messages from the database using QuerySet.
def allMsgs(request):
    title = 'All Messages'
    title_align_center = True
    form = allMsgsForm(request.POST or None)
    context = {
    "form": form,
    "title": title,
    "title_align_center": title_align_center,
    }
    if request.user.is_authenticated() and request.user.is_staff:
        queryset = msg.objects.all().order_by('-timestamp')
    context = {
        "queryset": queryset
    }
    return render(request, "allMsgs.html", context)


#Home Funtion Definition
def about (request):
    return render(request, "about.html", {})
