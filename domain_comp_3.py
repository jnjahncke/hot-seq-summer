#!/usr/bin/env python3

# Input: 3 lists of enriched domains in diff exp genes of species1, 2 and 3
# 
# Output: which domains are enriched in all lists?

import sys

def read_domains(test_file1, test_file2, test_file3):
	# reads the three files, creates three lists of domains
	diff_domains1 = []
	diff_domains2 = []
	diff_domains3 = []
	with open(test_file1,"r") as test1, open(test_file2,"r") as test2, open(test_file3,"r") as test3:
		
		for line in test1:
			line = line.rstrip()
			diff_domains1.append(line)

		for line in test2:
			line = line.rstrip()
			diff_domains2.append(line)

		for line in test3:
			line = line.rstrip()
			diff_domains3.append(line)

	return(diff_domains1, diff_domains2, diff_domains3)


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
	test_file3 = sys.argv[3]

	# read files, create domain lists
	diff_domains1, diff_domains2, diff_domains3 = read_domains(test_file1, test_file2, test_file3)	

	# shared domains
	shared = set(diff_domains1) & set(diff_domains2) & set(diff_domains3)

	# domains only in list1
	only_1 = set(diff_domains1) - set(diff_domains2) - set(diff_domains3)

	# domains only in list2
	only_2 = set(diff_domains2) - set(diff_domains1) - set(diff_domains3)

	# domains only in list3
	only_3 = set(diff_domains3) - set(diff_domains1) - set(diff_domains2)

	print(f'''# list1:\t{test_file1}
# list2:\t{test_file2}
# list3:\t{test_file3}
# list1 (all):\t{len(diff_domains1)}
# list2 (all):\t{len(diff_domains2)}
# list3 (all):\t{len(diff_domains3)}
# shared:\t{len(shared)}
# only in list1:\t{len(only_1)}
# only in list2:\t{len(only_2)}
# only in list3:\t{len(only_3)}
# 
# Shared enriched domains:''')

	# Make pfam_id:description dictionary
	pfam_dict = pfam_list_to_dict("RawData/pfam2desc.txt")

	# Look up pfam descriptions for each pfam ID
	shared_descriptions = pfam_id_to_desc(shared, pfam_dict)
	[print(desc) for desc in shared_descriptions]


if __name__ == "__main__":
	main()
