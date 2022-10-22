#!/usr/bin/env python3

import sys

oma_file = sys.argv[1]
oma_ens_file = sys.argv[2]
oma_dict = {}
o2e_dict = {}

## create a curated data set for oma groups for just the species of interest
with open(oma_file, 'r') as file_obj:
	for line in file_obj:
		if '#' in line:
			continue
		else:
			line= line.rstrip()
			group_list = line.split('\t')
			oma_dict[group_list[0]] = group_list[2:]

print(oma_dict)
			
with open(oma_ens_file, 'r') as obj:
	for line in obj:
		if '#' in line:
			continue
		else:
			line = line.rstrip()
			acc_list = line.split('\t')
			o2e[acc_list[0]] = 
			




