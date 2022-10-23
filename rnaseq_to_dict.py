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
      lineNum = 1
      for line in rnaseq_file:
        line = line.rstrip()
        geneID, valueLFC, valueP = line.split('\t')

        # Skip the header
        if lineNum == 1:
          lineNum += 1
          next
    
        # Create a new filename key and add entry to dictionary
        elif rnaseq_file not in combined_rnaseq_dict:
          combined_rnaseq_dict[rnaseq_file] = {}
          combined_rnaseq_dict[rnaseq_file][geneID] = [float(valueLFC), float(valueP)]

        # Add entry to existing filename key
        else:
          combined_rnaseq_dict[rnaseq_file][geneID] = [float(valueLFC), float(valueP)]
          
  return(combined_rnaseq_dict)






def main():
  
  # Process any number of RNAseq files
  multi_species_rnaseq_dict = (rnaseqs_to_dict(sys.argv[1:]))
  
  # Dictionary with data from all input files featured
  return(multi_species_rnaseq_dict)

if __name__ == '__main__':
  main()  
