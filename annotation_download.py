#!/usr/bin/env python3
from pybiomart import Dataset
import pandas as pd
import numpy as np
import sys, os
import math
import re



### Returns seaparate dictionaries: key=Ensembl stable geneID values=list of pfam IDs for protein domains ###



def species_domain_dict():

  # Species list to modify the query to Ensembl Genes 108 database--common names: human, mouse, yeast
  #speciesList =  ['hsapiens', 'mmusculus', 'scerevisiae']
  speciesList =  ['scerevisiae']

  # Run a query for each species
  for species in speciesList:

    # A Dataset instance can be constructed directly if the name of the dataset and the url of the host are known
    dataset = Dataset(name=f"{species}_gene_ensembl", host='http://www.ensembl.org')

    # Biomart server query returns a dataframe of 2 columns: 'Gene stable ID' and 'Pfam ID'
    dfID = dataset.query(attributes=['ensembl_gene_id', 'pfam'])
    # Remove nonvalues [nan] from dataframe
    dfIDs = dfID.dropna()

    # Pull the dataframe columns into a list of lists (gene ID and Pfam pairs)
    idArray = dfIDs.to_numpy()   

 
    # Parse array into a dictionary 
    annotationDict = {}
    for idList in idArray:
      geneID = idList[0]
      pfamID = idList[1]
      
      # Add pfam ID to an existing gene ID key
      if geneID in annotationDict:
        annotationDict[geneID].append(pfamID)
      
      # For a new key, establish a list and add the pfam
      else:
        annotationDict[geneID] = []
        annotationDict[geneID].append(pfamID)

  # A separate dictionary is returned for each species
  return(annotationDict)



def main ():
 #Remove print after troubleshooting
 print(species_domain_dict())


if __name__ == '__main__':
  main()



