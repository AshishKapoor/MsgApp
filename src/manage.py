#!/usr/bin/env python
#**********************************************************************#
# File Name: manage.py
# Writen By: Ashish Kapoor
# Comment: ("Django is AWESOME!")
# Project Name: Activity for Zenatix
# Purpose of this file: The Manager __aka__ The Runner
#**********************************************************************#

#insert your imports here
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trydjango18.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
