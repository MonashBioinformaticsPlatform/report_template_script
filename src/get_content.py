#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import re

def get_title(markdown_file):
    
    title = ''

    for i in open(markdown_file):
        line = i.strip()
        tcheck_one = re.search('(^[#][A-z0-9])', line)
        tcheck_two = re.search('(^[#]\W[A-z0-9])', line)
        if tcheck_one or tcheck_two:
            title = line.strip("#").strip()

    return title

def get_content(markdown_file):

    body = ''
    summary = ''
    summary_header = False

    title = get_title(markdown_file)

    for i in open(markdown_file):
        line = i.strip()

        line_check = line.replace(' ', '').lower().startswith('##summary')
        if line_check:
            summary_header = True
    
        if line.startswith('#') and not line_check:
            summary_header = False
    
        if summary_header:
            if '## Summary' in summary or '##Summary' in summary:
                summary = ''
            summary += line+'\n'
        else:
            body += line+'\n'

    return title, summary, body
