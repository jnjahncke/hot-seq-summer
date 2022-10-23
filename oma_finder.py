#!/usr/bin/env python3

import sys 
from oma_to_dict import *

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

## define the function to convert a list of ensemble IDs to oma IDs
def convert_to_oma(ens_list):
	oma_list = []
	for oma_ID in o2e_dict:
		for gene in ens_list:
			if gene == o2e_dict[oma_ID]:
				oma_list.append(oma_ID)
	return(oma_list)

## define the functino for taking a list of oma ID and grabbing the oma_group they belong to, storing them in a set
def find_oma_groups(oma_list):
	oma_groups = set()
	for oma_ID in oma_dict:
		for gene in oma_list:
			if gene == oma_ID:
				oma_groups.add(oma_dict[oma_ID])
	return(oma_groups)

## Define the input for the DEG files you want to compare
## DEG files must be in the format: ensemble_ID<tab>logFC<tab>pvalue
sp1_infile = sys.argv[1]
sp2_infile = sys.argv[2]

print(f'''
The deg file for species 1 is: {sp1_infile}
The deg file for species 2 is: {sp2_infile}''')

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
			data2 = line.split('\t')
			sp2_data[data2[0]] = {'logFC' : float(data2[1]) , 'pvalue' : float(data2[2])}

print(f'''
The deg data have been put into dictionaries''')

## read in the oma groups into a dictionary
## oma_dict format: omaID : oma_group
oma_dict = make_oma_dict()

## read in the oma ID to ens ID conversion dict
o2e_dict = omaID_to_ensID()

## create a list of up and down regulated genes for each species using the deg_list function defined above, store the lists in new variables
up1_ensID, down1_ensID = deg_list(sp1_data)
up2_ensID, down2_ensID = deg_list(sp2_data)

print(f'''
Up and down reg genes have been found for both species''')

## convert the list of ensemble IDs to a list of oma IDs using the function defined above
up1_omaID = convert_to_oma(up1_ensID)
down1_omaID = convert_to_oma(down1_ensID)
up2_omaID = convert_to_oma(up2_ensID)
down2_omaID = convert_to_oma(down2_ensID)

## find the oma groups for each deg list using the function defined above
up1_oma_groups = find_oma_groups(up1_omaID)
down1_oma_groups = find_oma_groups(down1_omaID)
up2_oma_groups = find_oma_groups(up2_omaID)
down2_oma_groups = find_oma_groups(down2_omaID)




