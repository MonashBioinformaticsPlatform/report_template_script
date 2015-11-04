# This is in-house report generation script

## Installation

No installation required just get it and run it with `-h` option

## Usage

```Python
mbp_report.py -m report.md -n $USER -e$USER@$$HOSTNAME.whatever
```	

Both `-n` and `-e` are options, whereas `-m` is mandatory !

This script will recognise your markdown file and convert into html report. Two simple rule for auto
detecting your project summary and project title. Title must start with a single hash character e.g `# This is your title` and all other major heading need to start with two hash characters e.g `## Summary`, `## Conmments`, `## Further work`, `## Whatever`


