# This is in-house report generation script

## Installation

No installation is required just get it and run it with `-h` option

## Usage

```Python
mbp_report.py -m report.md -n $USER -e $USER@$$HOSTNAME.whatever
```	

Both `-n` and `-e` are optional, whereas `-m` is mandatory !

This script will recognise your markdown file and convert it into html report. Two simple rules for auto
detecting your **project summary** and **project title**. **Title** must start with a single hash character e.g `# This is your title` and all other major headings must to start with two hashes characters e.g `## Summary`, `## Conmments`, `## Further work`, `## Whatever`


