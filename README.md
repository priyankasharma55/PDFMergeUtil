# PDFMergeUtil

PDFMergeUtil is a command line tool(CLI) written in Python based on PyPDF2 library(homepage: https://pypi.org/project/PyPDF2/).
This util helps you merge multiple PDF documents into a single file from command line.

## Prequisites
Install the PyPDF2 library using pip 
#### pip install PyPDF2

## How to run and usage

Input PDFs should be in the same directory as PDFMergeUtil.py and Output PDF will be generated in the same directory

    >PDFMergeUtil.py --help

    usage: PDFMergeUtil [-h] [-i [INPUT [INPUT ...]]] [-o OUTPUT] [-v]

    Command line utility for merging PDF files

    optional arguments:
      -h, --help            show this help message and exit
      -i [INPUT [INPUT ...]], --input [INPUT [INPUT ...]]
                            input files to be merged
      -o OUTPUT, --output OUTPUT
                            output file
      -v, --verbose         increase output verbosity
      
      




