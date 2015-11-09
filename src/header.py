#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

from argparse import ArgumentParser
from get_html import  render_markdown_content, process_r_markdown
from get_content import get_content, get_title

def get_args():
    parser = ArgumentParser(usage='%(prog)s -m markdown_file <path/to/your_md_file>',
                            description = 'Monash Bioinformatics Platform (MBP) Report Generator',
                            epilog = 'Author: Steve Androulakis <steve.androulakis@monash.edu>',
                            add_help = True
                            )
    
    parser.add_argument("-m", "--markdown_file",
                        help="Path to the markdown file content",
                        required = True,
                        dest="markdown_file",
                        metavar="YOUR_MARKDOWN_FILE"
                        )
    
    parser.add_argument("-n", "--name",
                        help="Report author name",
                        dest="name",
                        metavar="YOUR_NAME"
                        )
    
    parser.add_argument("-e", "--email",
                        help="Report author email",
                        default = 'steve.androulakis@monash.edu',
                        dest="email",
                        metavar="YOUR_EMAIL"
                        )
    
    parser.add_argument("-c", "--no_contents",
                        help="No table of contetns",
                        action='store_true',
                        dest="no_contents",
                        )
    
    args = parser.parse_args()
    
    md_file = args.markdown_file
    name = args.name
    email = args.email
    no_contents = args.no_contents

    return md_file, name, email, no_contents
