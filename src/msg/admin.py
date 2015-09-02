#!/usr/bin/env python
#**********************************************************************#
# File Name: admin.py
# Writen By: Ashish Kapoor
# Project Name: Activity for Zenatix
# Purpose of this file: Predefined Administration from Django framework.
#**********************************************************************#


#Insert your imports here
from django.contrib import admin
# Register your models here.
from .forms import msgForm
from .models import msg

class msgAdmin(admin.ModelAdmin):
    list_display = ["full_name","__str__","timestamp","updated"]
    form = msgForm

admin.site.register(msg, msgAdmin)
