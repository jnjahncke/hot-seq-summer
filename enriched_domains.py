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
# these two imports are just to get sample data
from mus_sampledata import *
from mus_sampledomains import *

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



def main():

	# Check for appropriate command line input
	progname = sys.argv[0]
	usage = f'\n\n\tusage: {progname} <up or down>'
	
	if len(sys.argv) < 2:
		sys.stderr.write(usage)
		sys.exit(1)

	# define direction (up/down), gene dictionary, and domain dictionary
	diff_direction = sys.argv[1]
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

	# Loop through hypergeometry() function
	if diff_direction.lower() == "up":
		# Print out p-values for upregulated domains
		print("# Domains in upregulated genes:")
		for domain in set(domains_all):
			print(f'{domain}\t{hypergeometry(domain, domains_all, domains_upreg)}')
	elif diff_dicrection.lower() == "down":
		# Print out p-values for downregulated domains
		print("# Domains in downregulated genes:")
		for domain in set(domains_all):
			print(f'{domain}\t{hypergeometry(domain, domains_all, domains_downreg)}')

	sys.exit(0)

if __name__ == "__main__":
	main()
