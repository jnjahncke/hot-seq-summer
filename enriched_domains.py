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

# these two imports are just to get sample data
from mus_sampledata import *
from mus_sampledomains import *

gene_dict = mus_sampledata() # this is sample data
domain_dict = mus_sampledomains() # this is sample data

# Determine upregulated/downregulated genes:
#	Upregulated: pvalue < 0.05, logFC > 0
#	Downregulated: pvalue < 0.05, logFC < 0
domains_upreg = []
domains_downreg = []
num_up = 0
num_down = 0
for gene in gene_dict:
	if gene_dict[gene]["pvalue"] < 0.05:
		if gene_dict[gene]["logFC"] > 0:
			num_up += 1
			for domain in domain_dict[gene]:
				domains_upreg.append(domain)
		if gene_dict[gene]["logFC"] < 0:
			num_down += 1
			for domain in domain_dict[gene]:
				domains_downreg.append(domain)

# Determine if domains in up/downregulated genes are enriched above chance
# First: what is the set of all the possible domains we could have pulled? (One of each domain)
domains_all = []
for gene in domain_dict:
	for domain in domain_dict[gene]:
		domains_all.append(domain)
domains_all = set(domains_all)
