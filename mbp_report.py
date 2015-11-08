#!/usr/bin/env python
####
# Monash Bioinformatics Platform Template Script 1.2
####
#   steve.androulakis@monash.edu
####
## Note: Set template_dir in run()!

from __future__ import print_function
import sys, re
import markdown
import subprocess
from jinja2 import Environment, FileSystemLoader


def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

def render_markdown_content(content):

    data = markdown.markdown(content,\
        extensions=['markdown.extensions.fenced_code'])

    return data

def process_r_markdown(rmarkdownfile):
    command = "Rscript -e \'require(knitr);" +\
    "opts_knit$set(out.format = \"md\"); knit(\"%s\")\'" % (rmarkdownfile)

    warning(subprocess.Popen(command, shell=True,
        stdout=subprocess.PIPE).stdout.read())

    filename = rmarkdownfile.rsplit('.')[0].rsplit('/')[-1]
    filename = "%s.md" % filename

    return filename

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

def run(): #### # Monash Bioinformatics Platform Template Script 1.2
    ####
    #   steve.androulakis@monash.edu
    ####
    template_dir = '/software/apps/report_template_script/templates'

    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-m", "--markdown_file", dest="markdown_file",
                      help="Path to the markdown file content",
                      metavar="MARKDOWNFILE")
    parser.add_option("-n", "--name", dest="name",
                      help="Report author name", metavar="NAME")
    parser.add_option("-e", "--email", dest="email",
                      help="Report author email", metavar="EMAIL")
    parser.add_option("-c", "--no_contents", dest="no_contents",
                      action='store_true',
                      help="No table of contents", metavar="NOCONTENTS")
    parser.add_option("-a", "--no_contact", dest="no_contact",
                      action='store_true',
                      help="No contact email (still inserted in html comments)", metavar="NOCONTACT")

    (options, args) = parser.parse_args()

    if not options.markdown_file:
        print("Bioinformatics Platform Template Generator")
        print("Steve Androulakis <steve.androulakis@monash.edu>")
        print("Eg. python bioinformatics_template_markdown.py -m markdown_file.md " \
        " -n 'Steve Androulakis'" \
        " -e steve.androulakis@monash.edu")
        print("")
        sys.exit()

    markdown_file = options.markdown_file
    name = options.name
    email = options.email
    no_contents = options.no_contents
    no_contact = options.no_contact

    title, summary, body = get_content(markdown_file)
    
    r = False
    # remove title from the body string
    filename = body.replace(title, '')

    if markdown_file[-3:].lower() == 'rmd':
        warning('RMD file detected. Processing...')
        r = True
        filename = process_r_markdown(markdown_file)

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('report_template.html')
    output_from_parsed_template = template.render(\
        content=render_markdown_content(filename),
        title=title,
        summary=summary,
        author_name=name,
        author_email=email,
        no_contents=no_contents,
        no_contact=no_contact,
        r=r)

    return output_from_parsed_template

if __name__ == "__main__":
    print(run())
