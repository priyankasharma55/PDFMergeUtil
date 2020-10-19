#!/usr/bin/python
# PDFMergeUtil
# Command line util to merge pdf files

import argparse
import PyPDF2

parser = argparse.ArgumentParser( prog = "PDFMergeUtil", description = "Command line utility for merging PDF files" )
parser.add_argument( "-i", "--input", help = "input files to be merged", nargs = '*' ) 
parser.add_argument( "-o", "--output", help = "output file" )
parser.add_argument( "-v", "--verbose", action="store_true", help="increase output verbosity")
args = parser.parse_args()

merger = PyPDF2.PdfFileMerger()
for file in args.input:
    merger.append( file )

merger.write( args.output )

if args.verbose:
    print( "Files merged and output file is {}".format( args.output ) )
else:
    print( args.output )    


