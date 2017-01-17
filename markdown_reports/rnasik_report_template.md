# Project title

## Professor X Researcher - Month Year

### Project summary 

The experiment was conducted on blah organism and examined y. There were x conditions with v samples to each one. 

(Include any interesting information about the experiment that the researcher has sent on - e.g aim of experiment, what they expect to see, what they are looking for, problems about particular samples, etc)

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;}
.tg .tg-cmwg{background-color:#ffccc9;text-align:center;vertical-align:top}
.tg .tg-r4if{background-color:#a6f2f4;text-align:center;vertical-align:top}
.tg .tg-d98o{font-weight:bold;background-color:#ffccc9;text-align:center}
.tg .tg-fs8v{font-weight:bold;background-color:#a6f2f4;text-align:center}
</style>
<table class="tg">
  <tr>
    <th class="tg-fs8v">Condition 1 - wildtype/control</th>
    <th class="tg-d98o">Condition 2 - mutant/treatment</th>
  </tr>
  <tr>
    <td class="tg-r4if">sample 1</td>
    <td class="tg-cmwg">sample 1</td>
  </tr>
  <tr>
    <td class="tg-r4if">sample 2</td>
    <td class="tg-cmwg">sample 2</td>
  </tr>
  <tr>
    <td class="tg-r4if">sample 3</td>
    <td class="tg-cmwg">sample 3</td>
  </tr>
</table>
*Table 1. Experimental design*

[I use this website to generate html tables](http://www.tablesgenerator.com/html_tables#)

### Data processing

Summarise the pipeline workflow. At the end, link to a Rnotebook that documents the commands run

To process the raw data, the [RNAsik pipeline](https://github.com/MonashBioinformaticsPlatform/RNAsik-pipe) was run on the fastq files. It used [STAR](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3530905/) for aligning the fastq files to the [organism of interest's genome](http://asia.ensembl.org/info/data/ftp/index.html). [FeatureCounts](http://bioinformatics.oxfordjournals.org/content/30/7/923.long) was then used to count reads to the [annotated features](http://asia.ensembl.org/info/data/ftp/index.html) in the genome. 

(Note the reference and gtf version and link directly to which ensembl file used. Perhaps make available in the workflow Rnotebook a copy of the reference used in case ensembl releases/updates a new reference)

[Link to workflow notebook](http://bioinformatics.erc.monash.edu/home/adele/templates/rnasik_template/rnasik_workflow_template.nb.html)

### Quality control

Mapping rates were x, with about ~xx% reads aligning to the genome on average across samples (see Table blah / Multiqc report table x). About y% fo reads were assigned to a feature (see Table blah)

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg .tg-69rz{font-weight:bold;background-color:#a6f2f4}
.tg .tg-xy75{font-weight:bold;background-color:#ffccc9;vertical-align:top}
.tg .tg-e3zv{font-weight:bold}
.tg .tg-x9ce{background-color:#a6f2f4}
.tg .tg-i6eq{background-color:#ffccc9;vertical-align:top}
.tg .tg-hk8o{font-weight:bold;background-color:#a6f2f4;vertical-align:top}
.tg .tg-xc13{background-color:#a6f2f4;vertical-align:top}
</style>
<table class="tg">
  <tr>
    <th class="tg-e3zv">Sample Name</th>
    <th class="tg-69rz">Sample 1 - WT</th>
    <th class="tg-hk8o">Sample 2 - WT</th>
    <th class="tg-hk8o">Sample 3 - WT</th>
    <th class="tg-xy75">Sample 1 - mutant</th>
    <th class="tg-xy75">Sample 2 - mutant</th>
    <th class="tg-xy75">Sample 3 - mutant</th>
  </tr>
  <tr>
    <td class="tg-e3zv">% Aligned to the genome</td>
    <td class="tg-x9ce">x</td>
    <td class="tg-xc13">x</td>
    <td class="tg-xc13">x</td>
    <td class="tg-i6eq">v</td>
    <td class="tg-i6eq">v</td>
    <td class="tg-i6eq">v</td>
  </tr>
  <tr>
    <td class="tg-e3zv">% Assigned to a feature</td>
    <td class="tg-x9ce">x</td>
    <td class="tg-xc13">x</td>
    <td class="tg-xc13">x</td>
    <td class="tg-i6eq">v</td>
    <td class="tg-i6eq">v</td>
    <td class="tg-i6eq">v</td>
  </tr>
</table>
*Table 2 (optional). Summary of relevant QC statistics that might be interesting based on the experiment*

* [MultiQC report for samples](link to MultiQC)

Describe any odd QC statistics / investigations in the data.

### Differential Expression

The counts from the dataset was loaded into [Degust](http://dna.med.monash.edu:4000/) for differential expressions analyis. A minimum of x counts per million (CPM) in at least y samples was set as a filter:

* [Degust report](link to Degust)

Discuss MDS clustering, anything interesting/problematic samples, etc

#### How to use Degust:

(Instructions!)


### Additional analyses:

* [IGV links]()
* [Custom plots, e.g heatmaps]() - Link to a Rnotebook that was used to generate any custom plots (because of course you used R for this, right)
* [Custom shiny app]() - could have a standlone app if complicated or if simple - could embed it into a Rmarkdown document that details the app's code


(Then to turn this markdown document into a report:

`/home/kirill/gitrepos/report_template_script/src/mbp_report.py -m index.md -n your_name -e your_name@monash.edu --no_contents > index.html
`

Someday, will sort out the bit with the table of contents :) )

* [Download this as a markdown file](http://bioinformatics.erc.monash.edu/home/adele/templates/rnasik_template/rnasik_report_template.md)