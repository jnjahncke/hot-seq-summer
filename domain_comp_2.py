#!/usr/bin/env python3

# Input: 2 lists
#	List of enriched domains in diff exp genes of species1
#	List of enriched domains in diff exp genes of species2
# 
# Output: which domains are enriched in both lists?

import sys

def read_domains(test_file1, test_file2):
	# reads the two files, creates two lists of domains
	diff_dict1 = {}
	diff_domains1 = []
	diff_dict2 = {}
	diff_domains2 = []
	with open(test_file1,"r") as test1, open(test_file2,"r") as test2:
		
		for line in test1:
			line = line.rstrip().split("\t")
			diff_dict1[line[0]] = float(line[1])
			diff_domains1.append(line[0])

		for line in test2:
			line = line.rstrip().split("\t")
			diff_dict2[line[0]] = float(line[1])
			diff_domains2.append(line[0])

	return(diff_domains1, diff_domains2)


def pfam_list_to_dict(pfam_file):
# Read in pfam file with <pfam id> \t <description> and make a dictionary
	pfam_dict = {}
	with open(pfam_file,"r") as infile:
		for line in infile:
			line = line.rstrip().split("\t")
			pfam_dict[line[0]] = line[1]
	return(pfam_dict)


def pfam_id_to_desc(pfamID_list, pfam_dict):
# input: LIST of pfam IDs, pfam dictionary from pfam_list_to_dict
# output: LIST of pfam descriptions
	desc_list = []
	[desc_list.append(pfam_dict[ID]) for ID in pfamID_list]
	return(desc_list)

def main():

	# Inputs: two .txt files generated from enriched_domains.py
	test_file1 = sys.argv[1]
	test_file2 = sys.argv[2]

	# read files, create domain lists
	diff_domains1, diff_domains2 = read_domains(test_file1, test_file2)	

	# shared domains
	shared = set(diff_domains1) & set(diff_domains2)

	# domains only in list1
	only_1 = set(diff_domains1) - set(diff_domains2)

	# domains only in list2
	only_2 = set(diff_domains2) - set(diff_domains1)

	print(f'''# list1:\t{test_file1}
# list2:\t{test_file2}
# list1 (all):\t{len(diff_domains1)}
# list2 (all):\t{len(diff_domains2)}
# shared:\t{len(shared)}
# only in list1:\t{len(only_1)}
# only in list2:\t{len(only_2)}
# 
# Shared enriched domains:''')

	# Make pfam_id:description dictionary
	pfam_dict = pfam_list_to_dict("RawData/pfam2desc.txt")

	# Look up pfam descriptions for each pfam ID
	shared_descriptions = pfam_id_to_desc(shared, pfam_dict)
	[print(desc) for desc in shared_descriptions]


if __name__ == "__main__":
	main()
