#!/usr/bin/env python3

# Input: 2 lists
#	List of enriched domains in diff exp genes of species1
#	List of enriched domains in diff exp genes of species2
# 
# Output: which domains are enriched in both lists?

import sys

# Inputs: two .txt files generated from enriched_domains.py
test_file1 = sys.argv[1]
test_file2 = sys.argv[2]

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

# shared domains
shared = set(diff_domains1) & set(diff_domains2)

# only in list1
only_1 = set(diff_domains1) - set(diff_domains2)

# only in list2
only_2 = set(diff_domains2) - set(diff_domains1)

print(f'''list1 (all): {len(diff_domains1)}
list2 (all): {len(diff_domains2)}
shared: {len(shared)}
list1 (only): {len(only_1)}
list2 (only): {len(only_2)}''')

print("\nDo you want a list of domains?")
print("Choices: (0 = no list), (1 = domains unique to list1), (2 = domains unique to list2), (3 = shared domains)")
todo = int(input("Type your choice here: "))
while todo > 0:
	if todo == 1:
		print(only_1)
		todo = int(input("Type another choice: "))
	elif todo == 2:
		print(only_2)
		todo = int(input("Type another choice: "))
	elif todo == 3:
		print(shared)
		todo = int(input("Type another choice: "))
	else:
		todo = 0
		pass
