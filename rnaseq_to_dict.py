#!/usr/bin/env python3
import os, sys
import re



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
  
  # Process any number of RNAseq files
  multi_species_rnaseq_dict = (rnaseqs_to_dict(sys.argv[1:]))
  
  # Dictionary with data from all input files featured
  return(multi_species_rnaseq_dict)

if __name__ == '__main__':
  main()  
