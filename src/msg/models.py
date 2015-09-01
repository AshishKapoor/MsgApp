#!/usr/bin/env python
#**********************************************************************#
# File Name: models.py
# Writen By: Ashish Kapoor
# Project Name: Activity for Zenatix
# Purpose of this file: Models are defined here.
#**********************************************************************#


#insert your imports here
from django.db import models

# Create your models here.
class msg(models.Model):
    message = models.CharField(max_length = 120, blank=False, null=True)
    full_name = models.CharField(max_length = 120, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self): #Python 2.7 uses __unicode__
        return self.message
