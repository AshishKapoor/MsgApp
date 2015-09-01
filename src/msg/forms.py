#!/usr/bin/env python
#**********************************************************************#
# File Name: forms.py
# Writen By: Ashish Kapoor
# Project Name: Activity for Zenatix
# Purpose of this file: Forms are defined here.
#**********************************************************************#

#insert your imports here
from django import forms
from .models import msg

class contactForm(forms.Form):
	full_name = forms.CharField(required=False)
	message = forms.CharField(required=False)


class msgForm(forms.ModelForm):
    class Meta:
        model = msg
        fields = ['full_name','message']
        #exclude = ['full_name']   #Other ways to exclude fields


def clean_full_name(self):
	full_name = self.cleaned_data.get('full_name')
	#write validation code.
	return full_name

class allMsgsForm(forms.Form):
	anything = forms.CharField(required=False)
