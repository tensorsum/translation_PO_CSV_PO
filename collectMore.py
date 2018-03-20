#!/usr/bin/python

from __future__ import print_function
import subprocess

#source = ({}, {} ...)

names = {}
for c in source:
    for (k,v) in c:
        names[v] = ''

with open("locale/en_US/LC_MESSAGES/django.po", "a") as f:
    print ('', file = f)
    for (n,t) in names.items():
        line = 'msgid "' + n + '"'
        out = subprocess.call(["grep", "-cxq", line, 'locale/en_US/LC_MESSAGES/django.po'])
        if out:
            print (line, file = f)
            print ('msgstr ""\n', file = f)
