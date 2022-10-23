#!/usr/bin/env python3

import sys

def make_oma_dict():
	oma_file = sys.argv[3]
	oma_dict = {}

## create a dictionary of oma accession numbers belonging to each oma group.
## oma_dict format: omaID : oma_group
	with open(oma_file, 'r') as file_obj:
		for line in file_obj:
			if '#' in line:
				continue
			else:
				line= line.rstrip()
				group_list = line.split('\t')
				for gene in group_list:
					if group_list.index(gene) == 0:
						continue
					else:
						oma_dict[gene] = group_list[0]

		print(f'''
Dictionary of genes belonging to oma groups complete!
key:value pairs are omaID : oma_group
''')
		return(oma_dict)


def omaID_to_ensID():
	oma_ens_file = sys.argv[4]
	o2e_dict = {}
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
	return(o2e_dict)

#def main():
#print(f'File meant to be run within another script')


#if __name__ = '__main__'
#	main()

