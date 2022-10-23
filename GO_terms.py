#! /usr/bin/env python3

# First install goatools using pip install goatools
import goatools 

### get the most recent GOAT tools library. This allows to parse the Gene Ontology (GO) OBO file.

#import OBO parser from GOATools
from goatools import obo_parser 


#in order to download GO OBO file also get wget and os. Install GO OBO first
import wget
import os


#We will download the OBO file into the folder './data'. We will download go-basic.obo which is acyclic.
go_obo_url = 'http://purl.obolibrary.org/obo/go/go-basic.obo'
data_folder = os.getcwd() + '/data'

#check if we have a ./data directory already
if(not os.path.isfile(data_folder)):
    try:
        os.mkdir(data_folder)
    except OSError as e:
        if(e.errno != 17):
            raise e
else:
    raise Exception(' + data_folder +') # !check if you can add description

#check if the file exists already
if(not os.path.isfile(data_folder+'/go-basic.obo')):
    go_obo = wget.download(go_obo_url, data_folder+'/go-basic.obo')
else:
    go_obo = data_folder+'/go-basic.obo' # the path is now stored in go_obo variable
print(go_obo)

#OBO parser with OBO library
go = obo_parser.GODag(go_obo)



### Open a dictonary with all genes and assosiated GO terms 
def read_annot(file_name):
	annot_dict = {}
	with open (file_name, 'r') as annot_file:
		next(annot_file)
		for line in annot_file:
			line =line.rstrip()
			fields = line.split("\t")
			if len(fields) == 2: 
				annot_dict[fields[0]] = fields[1]
	return annot_dict

annot_dict = read_annot("genes_assoc.txt")
#print(annot_dict)

pop = set(annot_dict.keys()) 

### Provide a list of genes of interest e.g. upregulated genes:
study = []
with 	open ('cell_differentiation.txt','r') as study_list:  
	next(study_list)
	for line in study_list:
		line = line.rstrip()
		study.append(line)
study = set(study)
###  Perfom GO enrichment analysis using GOEnrichmentStudy

methods = ["bonferroni", "sidak", "holm", "fdr"]

from goatools.go_enrichment import GOEnrichmentStudy
g = GOEnrichmentStudy(pop, annot_dict, go,
													propagate_counts=True,
													alpha=0.05,
													methods=methods)
g_res = g.run_study(study)
g.print_results(g_res, min_ratio=None, pval=0.01)
