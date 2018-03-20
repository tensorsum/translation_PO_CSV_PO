#!/usr/bin/python

from __future__ import print_function
import re
import csv

def decodeVars(line, var_dict, start_new_line, end_new_line):
    for (code,var) in var_dict.items():
        line = line.replace(code,var)
    return start_new_line + line + end_new_line

with open("locale/en_US/LC_MESSAGES/django.po") as f, open("translation_done.csv") as c, open('locale/de/LC_MESSAGES/django.po', 'w+') as d, open('locale/ru/LC_MESSAGES/django.po', 'w+') as r, open('locale/ja/LC_MESSAGES/django.po', 'w+') as j, open('locale/zh/LC_MESSAGES/django.po', 'w+') as z, open('locale/pt/LC_MESSAGES/django.po', 'w+') as p:
    reader = csv.reader(c)
    f_ind = 1
    for row in reader:
        ind = int(row[0])
        var_dict = {x[0] : x[1] for x in [x.split("=") for x in row[1].split(", ") ]} if ('=' in row[1]) else {}
        message = ''
        for i, line in enumerate(f, f_ind):
            if i >= ind :
                message = message.replace('"', '')
                start_new_line =  '\\n' if (re.match(r'^msgid[ ]*\\n[ ]*\S', message)) else ''
                end_new_line = '\\n' if (re.search(r'\S[ ]*\\n$', message)) else ''
                print ('###', message)

                print ('msgstr "' + decodeVars(row[3], var_dict, start_new_line, end_new_line) + '"', file=d)
                print ('msgstr "' + decodeVars(row[4], var_dict, start_new_line, end_new_line) + '"', file=r)
                print ('msgstr "' + decodeVars(row[5], var_dict, start_new_line, end_new_line) + '"', file=j)
                print ('msgstr "' + decodeVars(row[6], var_dict, start_new_line, end_new_line) + '"', file=z)
                print ('msgstr "' + decodeVars(row[7], var_dict, start_new_line, end_new_line) + '"', file=p)
                break
            if(line.startswith('msgid')): ## Line index found
                message = ''
            ln = line.strip()
            message += ln
            print (ln, file=d)
            print (ln, file=r)
            print (ln, file=j)
            print (ln, file=z)
            print (ln, file=p)
        f_ind = i+1
