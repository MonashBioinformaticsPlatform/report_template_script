# This is in-house report generation script

## Content

- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Usage](#usage)

## Installation

- `git clone https://github.com/MonashBioinformaticsPlatform/report_template_script.git`
- run `mbp_report.py`, which is located inside `src/` directory 

## Prerequisites

- [Jinja2](http://jinja.pocoo.org/docs/dev/) `pip install Jinja2`
- [Markdown](https://pythonhosted.org/Markdown/) `pip install markdown`

## Usage

```Python
mbp_report.py -m report.md -n $USER -e $USER@$$HOSTNAME.whatever
```	

Both `-n` and `-e` are optional, whereas `-m` is mandatory !

This script will recognise your markdown file and convert it into html report, using in-built html template. Two simple rules for auto detecting your **project summary** and **project title**. **Title** must start with a single hash character e.g `# This is your title` and all other major headings must start with two hashes characters e.g `## Summary`, `## Conmments`, `## Further work`, `## Whatever`
