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
    title = "Welcome"
    if request.user.is_authenticated():
        title = "%s" %(request.user)

        form = msgForm(request.POST or None)
        context = {
        "title": title,
        "form": form,
        }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Message sent! via MSG App')

    # if request.user.is_authenticated() and request.user.is_staff:
    #     queryset = msg.objects.all().order_by('-timestamp')
    #     context = {
    #         "queryset": queryset
    #     }

    return render(request, "home.html", context)

#Contact Function definition
def contact(request):
    title = 'Contact Us'
    title_align_center = True
    form = contactForm(request.POST or None)
    if form.is_valid():
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        print (form_message, form_full_name)

    context = {
    "form": form,
    "title": title,
    "title_align_center": title_align_center,
    }
    # if request.user.is_authenticated() and request.user.is_staff:
    #     queryset = msg.objects.all().order_by('-timestamp')
    # context = {
    #     "queryset": queryset
    # }
    return render(request, "forms.html", context)

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
