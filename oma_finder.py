#!/usr/bin/env python3

import sys 
from oma_to_dict import *
from rnaseq_to_dict import *


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

## define deg data files and the two species being compared
sp1_file = sys.argv[1]
sp2_file = sys.argv[2]
sp_file_list = [sp1_file, sp2_file]
sp1 = 'YEAST'
sp2 = 'MOUSE'

## put deg data into dictionary for 2 sp
sp1_data, sp2_data = rnaseqs_to_dict(sp_file_list)

print(sp1_data)
print(sp2_data)

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

print(f'up1 ens : {up1_ensID}')
print(f'up2 ens : {up2_ensID}')

print(f'''
Up and down reg genes have been found for both species
''')

## convert the list of ensemble IDs to a list of oma IDs using the function defined above
up1_omaID = convert_to_oma(up1_ensID)
#down1_omaID = convert_to_oma(down1_ensID)
up2_omaID = convert_to_oma(up2_ensID)
#down2_omaID = convert_to_oma(down2_ensID)
print(f'up1 omas : {up1_omaID}')
print(f'up2 omas : {up2_omaID}')

## find the oma groups for each deg list using the function defined above
up1_oma_groups = find_oma_groups(up1_omaID)
#down1_oma_groups = find_oma_groups(down1_omaID)
up2_oma_groups = find_oma_groups(up2_omaID)
#down2_oma_groups = find_oma_groups(down2_omaID)

print(up2_oma_groups)

## find the common oma groups up and down regulated in the species

#common_ups = up1_oma_groups & up2_oma_groups

#print(common_ups)






