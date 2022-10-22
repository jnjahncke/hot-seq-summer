#!/usr/bin/env python3
import sys, os
import pandas as pd
from pybiomart import Dataset
import numpy as np
import re
# chmod +x annotation_download.py



### Returns 



# List names and atrributes to modify the query for each species
# Common names: zebra fish, rat, chicken
speciesList =  ['drerio', 'rnorvegicus', 'ggallus']

# Pass in arguments later?
def annot_species_dict():

  # Run a query for each species
  for species in speciesList:

    # A Dataset instance can be constructed directly if the name of the dataset and the url of the host are known
    dataset = Dataset(name=f"{species}_gene_ensembl", host='http://www.ensembl.org')


    # Query the biomart server returns a df of 3 columns: index, 'Gene stable ID' and 'Pfam ID'
    dfIDs = dataset.query(attributes=['ensembl_gene_id', 'pfam'])


    # Pull the second and third columns into a list of lists (gene ID and Pfam pairs)
    # Remove nan values doesn't work yet    
    idArray = dfIDs.to_numpy()
    #idArray = idArrayNAN[~np.isnan(idArrayNAN)]
    
    # Parse array into a dictionary 
    # Will creat one for each species
    annotationDict = {}
    for idList in idArray:
      geneID = idList[0]
      pfamID = idList[1]
      
      # Skip over genes with no pfam entry
      if pfamID == 'nan':
        continue			### Still getting empty Pfam entries added to list with "" or "nan" ###
      
      # Add pfam ID to an existing gene ID key
      elif geneID in annotationDict:
        annotationDict[geneID].append(pfamID)
      
      # For a new key, establish a list and add the pfam
      else:
        annotationDict[geneID] = []
        annotationDict[geneID].append(pfamID)


  return(annotationDict)



def main ():
 #Remove print after troubleshooting
 print(annot_species_dict())


if __name__ == '__main__':
  main()



