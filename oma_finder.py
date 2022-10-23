#!/usr/bin/env python3

import sys 

## define the function to pull a list of significantly up and down regulated genes from a dictionary of DEG data
## input deg_data must be in the format: {ensemble_ID: {'logFC':value , 'pvalue' : value}}
def deg_list(deg_data):
	genes_up = []
	genes_down = []
	for gene in deg_data:
		if deg_data[gene]['pvalue'] < 0.05:
			if deg_data[gene]['logFC'] > 0:
				genes_up.append(gene)
			if deg_data[gene]['logFC'] < 0:
				genes_down.append(gene)
	return genes_up, genes_down

## Define the input for the DEG files you want to compare
## DEG files must be in the format: ensemble_ID<tab>logFC<tab>pvalue
sp1_infile = sys.argv[1]
sp2_infile = sys.argv[2]

## create empty dicts to be deg_dicts for each species
sp1_data = {}
sp2_data = {}

## lines 28-45 open each DEG file and converts the data into a deg_dict
## deg_dict format: {ensembleID: {'logFC':value , 'pvalue' : value}}
with open(sp1_infile, 'r') as file1_obj:
	for line in file1_obj:
		if '#' in line:
			continue
		else:
			line = line.rstrip()
			data = line.split('\t')
			sp1_data[data[0]] = {'logFC' : float(data[1]) , 'pvalue' : float(data[2])}

with open(sp2_infile, 'r') as file2_obj:
	for line in file2_obj:
		if '#' in line:
			continue
		else:
			line = line.rstrip()
			print(line)
			data2 = line.split('\t')
			sp2_data[data2[0]] = {'logFC' : float(data2[1]) , 'pvalue' : float(data2[2])}

## create a list of up and down regulated genes for each species using the deg_list function defined above, store the lists in new variables
up1, down1 = deg_list(sp1_data)
up2, down2 = deg_list(sp2_data)








