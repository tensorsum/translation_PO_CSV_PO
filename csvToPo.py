#!/usr/bin/python

from __future__ import print_function
import re
import csv

with open("locale/en_US/LC_MESSAGES/django.po") as f, open("translation_done.csv") as c, open('locale/de/LC_MESSAGES/django.po', 'w+') as d, open('locale/ru/LC_MESSAGES/django.po', 'w+') as r, open('locale/ja/LC_MESSAGES/django.po', 'w+') as j, open('locale/zh/LC_MESSAGES/django.po', 'w+') as z, open('locale/pt/LC_MESSAGES/django.po', 'w+') as p:
    reader = csv.reader(c)
    f_ind = 1
    for row in reader:
        ind = int(row[0])
        message = ''
        for i, line in enumerate(f, f_ind):
            if i >= ind :
                # fix for compilemessages command complains about "started/ended with new line"
                message = message.replace('"', '')
                start_new_line =  '\\n' if (re.match(r'^msgid[ ]*\\n[ ]*\S', message)) else ''
                end_new_line = '\\n' if (re.search(r'\S[ ]*\\n$', message)) else ''

                # 'replace' is a fix for what GoogleTranslate does to variables
                # but most likely you'll need to add some fixes manually
                print ('msgstr "' + start_new_line + row[2].replace('% (', ' %(') + end_new_line + '"', file=d)
                print ('msgstr "' + start_new_line + row[3].replace('% (', ' %(') + end_new_line + '"', file=r)
                print ('msgstr "' + start_new_line + row[4].replace('% (', ' %(') + end_new_line + '"', file=j)
                print ('msgstr "' + start_new_line + row[5].replace('% (', ' %(') + end_new_line + '"', file=z)
                print ('msgstr "' + start_new_line + row[6].replace('% (', ' %(') + end_new_line + '"', file=p)
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
