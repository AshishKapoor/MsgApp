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
    list_display = ["__str__","full_name","timestamp","updated"]
    form = msgForm
    # class Meta:
    #     model = msg
    
admin.site.register(msg, msgAdmin)
