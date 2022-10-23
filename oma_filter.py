#!/usr/bin/env python3

import sys

oma_file = sys.argv[1]
oma_ens_file = sys.argv[2]
oma_dict = {}
o2e_dict = {}

## create a dictionary of oma accession numbers belonging to each oma group for oma groups.
## key:value pairs are oma_group:[list of genes]
with open(oma_file, 'r') as file_obj:
	for line in file_obj:
		if '#' in line:
			continue
		else:
			line= line.rstrip()
			group_list = line.split('\t')
			oma_dict[group_list[0]] = group_list[2:]

print(f'''
Dictionary of genes belonging to oma groups complete!
key:value pairs are oma_group:[list of genes]
''')

## Read in the oma to ensemble accession number table to a dictionary
with open(oma_ens_file, 'r') as obj:
	for line in obj:
		if '#' in line:
			continue
		else:
			line = line.rstrip()
			acc_list = line.split('\t')
			o2e_dict[acc_list[0]] = acc_list[1]

print(f'''
Oma to ensemble accession dict done!
key:values are oma:ens
''')

orthos_ensID = {}

for group in oma_dict:
	gene_list = oma_dict[group]
	orthos_ensID[group] = []
	for gene in gene_list:
		orthos_ensID[group].append(o2e_dict)

print(orthos_ensID)


