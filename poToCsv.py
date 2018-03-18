#!/usr/bin/python

from __future__ import print_function
import re
import csv

def stripEnds(line):
    line = re.sub(r'^\n|\n$', ' ', line)
    line = line.replace('\\n', ' ')
    line = re.sub(r'\s+', ' ', line)
    line = re.sub(r'^[ ]|[ ]$', '', line)
    line = re.sub(r'^"|"$', '', line)
    return line

string = ""
with open("locale/en_US/LC_MESSAGES/django.po") as f, open('translations.csv', 'w') as c:
    writer = csv.writer(c)
    for i, line in enumerate(f, 1):
        if(line.startswith('#')):
            continue

        if(re.search('msgstr', line)): ## Line index found
            print (string)
            string = stripEnds(string)
            writer.writerow((i, string))
        elif(line.startswith('msgid')):
            line = line.replace('msgid "', '')
            line = stripEnds(line)
            string = line
        else:
          line = stripEnds(line)
          string += " " + line
