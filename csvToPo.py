#!/usr/bin/python

from __future__ import print_function
import re
import csv

with open("locale/en_US/LC_MESSAGES/django.po") as f, open("translation_done.csv") as c, open('locale/de/LC_MESSAGES/django.po', 'w+') as d, open('locale/ru/LC_MESSAGES/django.po', 'w+') as r, open('locale/ja/LC_MESSAGES/django.po', 'w+') as j, open('locale/zh/LC_MESSAGES/django.po', 'w+') as z, open('locale/pt/LC_MESSAGES/django.po', 'w+') as p:
    reader = csv.reader(c)
    f_ind = 1
    for row in reader:
        ind = int(row[0])
        for i, line in enumerate(f, f_ind):
            if i >= ind :
                print ('msgstr "' + row[2] + '"', file=d)
                print ('msgstr "' + row[3] + '"', file=r)
                print ('msgstr "' + row[4] + '"', file=j)
                print ('msgstr "' + row[5] + '"', file=z)
                print ('msgstr "' + row[6] + '"', file=p)
                break
            ln = line.strip()
            print (ln, file=d)
            print (ln, file=r)
            print (ln, file=j)
            print (ln, file=z)
            print (ln, file=p)
        f_ind = i+1
