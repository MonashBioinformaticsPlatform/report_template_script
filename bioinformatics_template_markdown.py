####
# Monash Bioinformatics Platform Template Script 1.2
####
#   steve.androulakis@monash.edu
####
## Note: Set template_dir in run()!

from __future__ import print_function
import sys
import markdown
import subprocess
from jinja2 import Environment, FileSystemLoader


def warning(*objs):
    print("WARNING: ", *objs, file=sys.stderr)


def render_markdown_content(filename):
    with open(filename, "r") as myfile:
        data = myfile.read()

    data = markdown.markdown(data,\
        extensions=['markdown.extensions.fenced_code'])
    return data


def process_r_markdown(rmarkdownfile):
    command = "Rscript -e \'require(knitr);" +\
    "opts_knit$set(out.format = \"md\"); knit(\"%s\")\'" % (rmarkdownfile)

    warning(subprocess.Popen(command, shell=True,
        stdout=subprocess.PIPE).stdout.read())

    filename = rmarkdownfile.rsplit('.')[0]
    filename = "%s.md" % filename

    return filename


def run():
    ####
    # Monash Bioinformatics Platform Template Script 1.2
    ####
    #   steve.androulakis@monash.edu
    ####
    template_dir = '/software/apps/report_template_script/templates'

    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("-m", "--markdownfile", dest="markdownfile",
                      help="Path to the markdown file content",
                      metavar="MARKDOWNFILE")
    parser.add_option("-t", "--title", dest="title",
                      help="Title of your report",
                      metavar="TITLE")
    parser.add_option("-s", "--summary", dest="summary",
                      help="Report summary", metavar="SUMMARY")
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

    if not options.markdownfile:
        print("Bioinformatics Platform Template Generator")
        print("Steve Androulakis <steve.androulakis@monash.edu>")
        print("Eg. python bioinformatics_template_markdown.py -m markdown_file.md " \
        " -t 'My Awesome Report'" \
        " -s 'A summary of my report!'" \
        " -n 'Steve Androulakis'" \
        " -e steve.androulakis@monash.edu")
        print("")
        sys.exit()

    markdownfile = options.markdownfile
    title = options.title
    summary = options.summary
    name = options.name
    email = options.email
    no_contents = options.no_contents
    no_contact = options.no_contact

    r = False
    filename = markdownfile

    if markdownfile[-3:].lower() == 'rmd':
        warning('RMD file detected. Processing...')
        r = True
        filename = process_r_markdown(markdownfile)

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
