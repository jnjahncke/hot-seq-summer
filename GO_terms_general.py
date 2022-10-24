#! /usr/bin/env python3

import goatools 
from goatools import obo_parser 
import wget
import os
import sys

from shared_functions import *


def main():
  go = import_OBO()


  file_dict = [["hsapiens_go_id.txt","HUMAN_genes.txt","Human"],["mmusculus_go_id.txt","mus_rna_seq_final.txt","Mouse"],["scerevisiae_go_id.txt","yeast_degs.txt","Yeast"]]
  for species in file_dict:
    annot_dict = read_annot("RawData/"+species[0])
	
 #  annot_dict = read_annot("RawData/hsapiens_go_id.txt")
    pop = set(annot_dict.keys()) 
    study_dict = rnaseqs_to_dict(["RawData/"+species[1]])
    study_up,study_down = deg_list(study_dict["RawData/"+species[1]])

    GO_enrichment(pop, annot_dict, go, study_up, species[2]+"_up") 
    GO_enrichment(pop, annot_dict, go, study_down, species[2]+"_down")

### function to import OBO a database with all GO terms. 
def import_OBO():
  go_obo_url = 'http://purl.obolibrary.org/obo/go/go-basic.obo'
  data_folder = os.getcwd() + '/data'

  if(not os.path.isfile(data_folder)):
      try:
          os.mkdir(data_folder)
      except OSError as e:
          if(e.errno != 17):
              raise e
  else:
      raise Exception(' + data_folder +') # !check if you can add description

  if(not os.path.isfile(data_folder+'/go-basic.obo')):
      go_obo = wget.download(go_obo_url, data_folder+'/go-basic.obo')
  else:
      go_obo = data_folder+'/go-basic.obo' # the path is now stored in go_obo variable
  print(go_obo)
  go = obo_parser.GODag(go_obo)
  return go   


### Creates a dictonary with all genes and assosiated GO terms 
def read_annot(file_name):
  annot_dict = {}
  with open (file_name, 'r') as annot_file:
    next(annot_file)
    for line in annot_file:
      line =line.rstrip()
      fields = line.split("\t")
      if len(fields) == 2: 
        if fields[0] not in annot_dict:
          annot_dict[fields[0]] = set()
        annot_dict[fields[0]].add(fields[1])
  return annot_dict


###  Perfom GO enrichment analysis using GOEnrichmentStudy
def GO_enrichment (pop, annot_dict, go, study, name): 
#  methods = ["bonferroni", "sidak", "holm", "fdr"]                 # you can a list of methods instead of just bonferroni

  from goatools.go_enrichment import GOEnrichmentStudy
  g_bonferroni = GOEnrichmentStudy(pop, annot_dict, go,
                                  propagate_counts=True,
                                  alpha=0.01,
                                  methods=['bonferroni'])
  g_bonferroni_res = g_bonferroni.run_study(study)

  s_bonferroni = []
  for x in g_bonferroni_res:
    if x.p_bonferroni <= 0.001:
      s_bonferroni.append((x.goterm.id,x.p_bonferroni, x.goterm.name)) # you can modify this parameters and print more things. You just need to dig into docomentation to find how they are called


	# write the results into a file
  with open (name+"_GO_results.txt","w") as f:
    f.write("GO_terms\tp-value\tdescription\n")
    for term in s_bonferroni:
      f.write(f'{term[0]}\t{term[1]}\t{term[2]}\n')
      return set(s_bonferroni[0]) 

if __name__ == "__main__":
  main()


