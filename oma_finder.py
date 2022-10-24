#!/usr/bin/env python3

import sys 
from oma_to_dict import *
from shared_functions import * 

## define the function to convert a list of ensemble IDs to oma IDs
## ens_list should be a list of ensemble IDs for the up or down regulated genes in a single species

def convert_to_oma(ens_list):
	
	oma_list = []
	for gene in ens_list:
		for oma_ID in o2e_dict:
			if gene == o2e_dict[oma_ID]:
				oma_list.append(oma_ID)
	return(oma_list)

## define the function for taking a list of oma ID and grabbing the oma_group they belong to, storing them in a set

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

## put deg data into dictionary for 2 sp
sp_data = rnaseqs_to_dict(sp_file_list)

print(f'''
The deg data have been put into a dictionary''')

## read in the oma groups into a dictionary
## oma_dict format: omaID : oma_group
oma_dict = make_oma_dict()

## read in the oma ID to ens ID conversion dict
o2e_dict = omaID_to_ensID()

## create a list of up and down regulated genes for each species using the deg_list function defined above, store the lists in new variable
exp_data ={}

for file in sp_data:
	
	exp_data[file] = {}
	exp_data[file]['up'] = []
	exp_data[file]['down'] = []
	exp_data[file]['up'],exp_data[file]['down'] = deg_list(sp_data[file])

print(f'''
Up and down reg genes have been found for both species
''')

up_exp_omaID = {}
down_exp_omaID = {}


## convert the list of ensemble IDs to a list of oma IDs using the function defined above
for file in exp_data:
	
	up_exp_omaID[file] = {}
	up_exp_omaID[file]['up'] = []	
	up_ensIDs = exp_data[file]['up']
	up_exp_omaID[file]['up'] = convert_to_oma(up_ensIDs)
	
	down_exp_omaID[file] = {}
	down_exp_omaID[file]['down'] = []
	down_ensIDs = exp_data[file]['down']
	down_exp_omaID[file]['down'] = convert_to_oma(down_ensIDs)

print(f'''
The up reg omas are found!
''')
print(f'''
The down reg omas are found!''')

up_groups = {}
down_groups = {}

## find the oma groups for each deg list using the function defined above
for file in up_exp_omaID:
	
	up_groups[file] = {}
	up_groups[file]['up'] = set()	
	omaIDs = up_exp_omaID[file]['up']
	up_groups[file] = find_oma_groups(omaIDs) 	

print(f'''
the up reg groups are found!
''')

for file in down_exp_omaID:

	down_groups[file] = {}
	down_groups[file]['down'] = set()
	oma_IDS = down_exp_omaID[file]['down']
	down_groups[file] = find_oma_groups(oma_IDS)

print(f'''
the down reg groups are found!
''')

## find the common oma groups up and down regulated in the species

common_ups = up_groups[sp1_file] & up_groups[sp2_file]
common_downs = down_groups[sp1_file] & down_groups[sp2_file]

print(f'''
Commonly up regulated and down regulated oma groups found!''')

