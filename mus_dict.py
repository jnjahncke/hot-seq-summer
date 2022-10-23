#!/usr/bin/env python3

# data from: https://elifesciences.org/articles/07687/
# GEO accession: GSE65636


def mus_dict():

	test_dict = {}
	with open("mus_rna_seq_final.txt","r") as mus_in:
		linenum = 0
		for line in mus_in:
			linenum += 1
			if linenum > 1:
				line = line.rstrip().split("\t")
				test_dict[line[0]] = {"logFC":float(line[1]), "pvalue":float(line[2])}

	return(test_dict)

def main():
	mus_dict()

if __name__ == '__main__':
	main()
