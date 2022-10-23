#!/usr/bin/env python3

# data from: https://elifesciences.org/articles/07687/
# GEO accession: GSE65636
# file: mus_rnaseq_data.xlsx 
# sheet: mRNA-seq Data
# columns: gene, HS135logFC, HS135PValue

import pandas as pd
import requests, sys, re, warnings
warnings.simplefilter("ignore")

# Need to look up ensembl IDs from gene names
def gene_name2id(gene, species):
	server = "http://rest.ensembl.org"
	ext = r"/xrefs/symbol/"+ species + "/" + gene + r"?"
	r = requests.get(server + ext, headers = {"Content-Type":"text"})
	if not r.ok:
		r.raise_for_status()
		sys.exit()
	ID = re.findall(r"id: (ENS\w+?)\n", r.text)[0]
	return(ID)

		

def main():

	rna_seq_data_in = pd.read_excel("mus_rnaseq_data.xlsx", sheet_name = "mRNA-seq Data")
	subset = rna_seq_data_in.loc[:,["gene","HS135logFC","HS135PValue"]]

	genes = []
	ensIDs = []
	species = "mus musculus"
	for row in range(0,9980):
		gene = subset.iloc[row,0]
		try:
			ID = gene_name2id(gene,species)
		except:
			ID = "NA"
		ensIDs.append(ID)
		genes.append(gene)

	ensIDs_df = pd.DataFrame({"gene":genes, "EnsID":ensIDs})
	rna_seq_data = pd.merge(ensIDs_df, subset)
	rna_seq_data = rna_seq_data.iloc[:,1:] # select all rows, eliminate first column (genes)
	rna_seq_data = rna_seq_data[(rna_seq_data['EnsID'] != "NA")] # filter out NAs
	rna_seq_data.to_csv("mus_rna_seq_final.txt", sep = "\t")

if __name__ == '__main__':
	main()
