#!/usr/bin/env python3

# data from: https://elifesciences.org/articles/07687/
# GEO accession: GSE65636
# file: mus_rnaseq_data.xlsx 
# sheet: mRNA-seq Data
# columns: gene, HS135logFC, HS135PValue

import pandas as pd
import warnings
warnings.simplefilter("ignore")

def mus_sampledata():
	rna_seq_data = pd.read_excel("mus_rnaseq_data.xlsx", sheet_name = "mRNA-seq Data")
	subset = rna_seq_data.loc[:,["gene","HS135logFC","HS135PValue"]]

	test_dict = {}
	for row in range(0,9980):
		test_dict[subset.iloc[row,0]] = {"pvalue":subset.iloc[row,2], "logFC":subset.iloc[row,1]}

	return(test_dict)

def main():
	mus_sampledata()

if __name__ == '__main__':
	main()
