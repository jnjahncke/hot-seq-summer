#!/usr/bin/env python3

# Inputs:
#	1: dictionary containing genes, p-value, log fold change
#	2: dictionary containing genes, domains
#
# Calculate:
#	Which genes are upregulated (or downregulated)?
#	For those genes, which domains are enriched?
#
# Output: list of enriched domains

import sys
from math import comb
from shared_functions import *

# Probability mass function
# Takes a specific domain, list of all domains, and a list of domains from diff expressed genes
# Probability that we have k or more occurrences of domain in up/downreg list
def hypergeometry(domain,domains_all,domains_diff):
	bigN = len(domains_all)
	n = len(domains_diff)
	bigK = domains_all.count(domain)
	k = domains_diff.count(domain)
	prob = 0
	for num in range(k,bigK+1):	
		prob += comb(bigK,num) * comb(bigN-bigK,n-num) / comb(bigN,n)
		if comb(bigK,num) * comb(bigN-bigK,n-num) / comb(bigN,n) < 0.0001:
			break
	return(prob)

# create domain dictionary
def make_domain_dict(species):
	domain_dict = {}
	with open("ProcessedData/" + species + "_pfam.txt","r") as file_in:
		for line in file_in:
			line = line.rstrip().split("\t")
			if line[0] not in domain_dict:
				domain_dict[line[0]] = [line[1]]
			else:
				domain_dict[line[0]].append(line[1])
	return(domain_dict)

# Take a gene dictionary, determine which genes are up or down regulated
	#	Upregulated: pvalue < 0.05, logFC > 0
	#	Downregulated: pvalue < 0.05, logFC < 0
def diff_exp_domains(gene_dict, domain_dict, direction):
	domains_diff = []
	num_diff = 0
	for gene in gene_dict:
		try:
			if direction.lower() == "up":
				if gene_dict[gene][1] < 0.05: # pvalue < 0.05
					if gene_dict[gene][0] > 0: # logFC > 0
						num_diff += 1
						for domain in domain_dict[gene]:
							domains_diff.append(domain)
			if direction.lower() == "down":
				if gene_dict[gene][1] < 0.05: # pvalue < 0.05
					if gene_dict[gene][0] < 0: # logFC < 0
						num_diff += 1
						for domain in domain_dict[gene]:
							domains_diff.append(domain)
		except:
			continue
	return(domains_diff)


def main():

	# Check for appropriate command line input
	progname = sys.argv[0]
	usage = f'\n\n\tusage: {progname} <up or down> <species>\n<species> = "mmusculus", "hsapiens", "scerevisiae"'
	
	if len(sys.argv) < 3:
		sys.stderr.write(usage)
		sys.exit(1)

	# parse inputs
	diff_direction = sys.argv[1]
	species = sys.argv[2]

	# get gene dict using rna_seqs_to_dict
	if species == "mmusculus":
		input_file = "RawData/mus_rna_seq_final.txt"
	elif species == "hsapiens":
		input_file = "RawData/HUMAN_genes.txt"
	elif species == "scerevisiae":
		input_file = "RawData/yeast_degs.txt"
	gene_dict = rnaseqs_to_dict([input_file]) # defned in rnaseq_to_dict.py
	gene_dict = gene_dict[list(gene_dict.keys())[0]]

	# Make dictionary comaining all domains for all genes in a species
	domain_dict = make_domain_dict(species) # defined above

	# For that species, make a list of all domains from differentially expressed genes
	domains_diff = diff_exp_domains(gene_dict, domain_dict, diff_direction) # defined above

	# Determine if domains in up/downregulated genes are enriched above chance
	# First: what are all the possible domains we could have pulled?
	domains_all = []
	for gene in domain_dict:
		for domain in domain_dict[gene]:
			domains_all.append(domain)

	# Loop through hypergeometry() function (defined above)
	# Print out p-values for differentially expressed domains that are enriched
	for domain in set(domains_all):
		prob = hypergeometry(domain, domains_all, domains_diff)
		if prob < 0.05:
			print(f'{domain}\t{prob}')

	sys.exit(0)

if __name__ == "__main__":
	main()
