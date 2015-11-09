#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

import markdown
import subprocess

def render_markdown_content(content):

    data = markdown.markdown(content,
                             extensions=['markdown.extensions.fenced_code']
                             )

    return data

def process_r_markdown(rmarkdownfile):

    command = "Rscript -e \'require(knitr);" +\
    "opts_knit$set(out.format = \"md\"); knit(\"%s\")\'" % (rmarkdownfile)

    warning(subprocess.Popen(command, shell=True,
        stdout=subprocess.PIPE).stdout.read())

    filename = rmarkdownfile.rsplit('.')[0].rsplit('/')[-1]
    filename = "%s.md" % filename

    return filename
