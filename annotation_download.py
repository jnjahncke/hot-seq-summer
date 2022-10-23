#!/usr/bin/env python3
from pybiomart import Dataset
import pandas as pd
import numpy as np
import sys, os
import math
import re



### Returns a tsv dataframe text file: Ensembl stable geneID values \t pfam protein domains *or* GO term IDs ###



def species_annotation_dict(species, annotation_type):

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






def main ():
 
  # Species options to modify the query to Ensembl Genes 108 database: hsapiens, mmusculus, scerevisiae
  # Annotation options for Ensembl query: pfam or go_id
  species = sys.argv[1].lower()
  annotation_type = sys.argv[2].lower()

  # Call the function to make the dictionary
  dict_to_write = species_annotation_dict(species, annotation_type)  
 
  # Because dictionaries take minutes to load, they are written to a file to avoid re-downloading 
  annotationDF_txt = open(f"{species}_{annotation_type}.txt", "w")

  
  # Write each key and list item to a line in the file, note the new line character
  for gene_id in dict_to_write.keys():							# Key
    for annotationID in range(len(dict_to_write[gene_id])):				# List		
      annotationDF_txt.write(f"{gene_id}\t{dict_to_write[gene_id][annotationID]}\n")		
  
  # Close file after writing finished
  annotationDF_txt.close()



if __name__ == '__main__':
  main()



