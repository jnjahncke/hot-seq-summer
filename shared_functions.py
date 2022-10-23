#!/usr/bin/env python3

from pybiomart import Dataset
import pandas as pd
import numpy as np
import sys, os
import math
import re



### Returns a tsv dataframe text file: Ensembl stable geneID values \t pfam protein domains *or* GO term IDs ###
def species_annotation_df(species, annotation_type):

  # A Dataset instance can be constructed directly if the name of the dataset and the url of the host are know
  dataset = Dataset(name=f"{species}_gene_ensembl", host='http://www.ensembl.org')

  # Biomart server query returns a dataframe of 2 columns: 'Gene stable ID' and 'Pfam ID'
  datasetDF = dataset.query(attributes=['ensembl_gene_id', annotation_type])
  # Remove nonvalues [nan] from dataframe
  datasetDF_nonan = datasetDF.dropna()

  # Pull the dataframe columns into a list of lists (gene ID and Pfam pairs)
  idArray = datasetDF_nonan.to_numpy()   

 
  # Parse array into a dictionary 
  annotationDict = {}
  for idList in idArray:
    geneID = idList[0]
    annotation = idList[1]
      
    # Add pfam ID to an existing gene ID key
    if geneID in annotationDict:
      annotationDict[geneID].append(annotation)
      
    # For a new key, establish a list and add the pfam
    else:
      annotationDict[geneID] = []
      annotationDict[geneID].append(annotation)

  # A separate dictionary is returned for each species
  return(annotationDict)




### Inputs a formatted text file with 3 columns of RNAseq data: Ensembl ID, log fold change, and p value
### Outputs an RNAseq nested dict with {key:filename: {key=geneID: value= [logFC, pvalue]}}
def rnaseqs_to_dict(rnaseq_files):

  # Establish an empty dictionary and obtain data by spliting the line into separate strings
  combined_rnaseq_dict = {}
  
  for file in rnaseq_files:
    with open(file, 'r') as rnaseq_file:
      next(rnaseq_file)
      for line in rnaseq_file:
        line = line.rstrip()

        # Create a new filename key and add entry to dictionary
        if file not in combined_rnaseq_dict:
          geneID, valueLFC, valueP = line.split('\t')
          combined_rnaseq_dict[file] = {}
          combined_rnaseq_dict[file][geneID] = [float(valueLFC), float(valueP)]

        # Add entry to existing filename key
        else:
          geneID, valueLFC, valueP = line.split('\t')
          combined_rnaseq_dict[file][geneID] = [float(valueLFC), float(valueP)]
          
  return(combined_rnaseq_dict)



def main():
  exit()
if __name__ == "__main__":
  main()
