#!/usr/bin/env python3

import sys

#def omaID_to_ensID():
oma_ens_file = sys.argv[1]
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
key:values are omaID : ensID
''')



