#!/usr/bin/env python3

# data from: https://elifesciences.org/articles/07687/
# GEO accession: GSE65636
# file: mus_rnaseq_data.xlsx 
# sheet: mRNA-seq Data
# columns: gene

import pandas as pd
from random import randrange

def mus_sampledomains():
	rna_seq_data = pd.read_excel("mus_rnaseq_data.xlsx", sheet_name = "mRNA-seq Data")

	fake_domains = list("abcdefghijklmnopqrstuvwxyz")

	test_dict = {}
	for row in range(0,9980):
		test_dict[rna_seq_data.iloc[row,0]] = [fake_domains[randrange(len(fake_domains))], fake_domains[randrange(len(fake_domains))], fake_domains[randrange(len(fake_domains))]]

	return(test_dict)

def main():
	mus_sampledomains()

if __name__ == '__main__':
	main()
