#!/usr/bin/env python

####
# Monash Bioinformatics Platform Template Script 1.2
####
#   steve.androulakis@monash.edu
####

from __future__ import print_function
from jinja2 import Environment, FileSystemLoader
import header, get_content, get_html
import os

def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)

def run(md_file,
        name,
        email,
        no_contents,
        template_dir
        ):

    title, summary, body = get_content.get_content(md_file)
    
    r = False
    # remove title from the body string
    filename = body.replace(title, '')

    if md_file[-3:].lower() == 'rmd':
        warning('RMD file detected. Processing...')
        r = True
        filename = process_r_markdown(md_file)

    #TODO the autoescape should really be True, but when set
    # to True, html doesn't render...
    env = Environment(loader = FileSystemLoader(template_dir), 
                                   autoescape = False
                                   )
    template = env.get_template('report_template.html')

    output_from_parsed_template = template.render(content=get_html.render_markdown_content(filename),
                                                  title=title,
                                                  summary=summary,
                                                  author_name=name,
                                                  author_email=email,
                                                  no_contents=no_contents,
                                                  r=r
                                                  )

    return output_from_parsed_template

if __name__ == "__main__":

    # get directory name of the script being run
    mbp_dir = os.path.dirname(__file__)
    # make path to templates directory
    #TODO There should be better solution then .replace()
    template_dir = os.path.join(mbp_dir, 'templates').replace('src/','')
    # get required arguments
    md_file, name, email, no_contents = header.get_args()

    print(run(md_file,
              name,
              email,
              no_contents,
              template_dir
              )
          )
