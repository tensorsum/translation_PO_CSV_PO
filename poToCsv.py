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

def exractVariables(line):
    line_vars = {}
    pattern = re.compile(r"%\(\w+\)s")
    items = re.findall(pattern, line)
    for i, item in enumerate(items):
        code = 'xxx' + str(i) + 'xxx'
        line = line.replace(item, code)
        line_vars[ code ] = item
    var_str = ', '.join(reversed(['%s=%s' % (c, v) for (c, v) in line_vars.items()]))
    return [line, var_str]


string = ""
with open("locale/en_US/LC_MESSAGES/django.po") as f, open('translations.csv', 'w') as c:
    writer = csv.writer(c)
    for i, line in enumerate(f, 1):
        if(line.startswith('#')):
            continue

        if(re.search('msgstr', line)): ## Line index found
            string = stripEnds(string)
            string,var_str = exractVariables(string)
            print (string, '>>>', var_str)
            writer.writerow((i, var_str, string))
        elif(line.startswith('msgid')):
            line = line.replace('msgid "', '')
            line = stripEnds(line)
            string = line
        else:
          line = stripEnds(line)
          string += " " + line
