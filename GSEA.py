#!/usr/bin/env python3
#pip install gseapy
import pandas as pd
import gseapy as gp
import matplotlib.pyplot as plt
from gseapy import Biomart
import csv
import numpy as np
import sys

#required inputs 
## data with: pandas.df, .gct format, .txt format; 
## cls with: a list, .cls format file

#read in gene list
gene_exp=pd.read_csv("mus_rnaseq_data.xlsx", sheet_name = "mRNA-seq Data", encoding='latin-1')

#phenoA, phenoB, class_vector =  gp.parser.gsea_cls_parser("mus_rnaseq_data.xlsx")
#print (class_vector)
#print("positively correlated: ", phenoA)
#print("negtively correlated: ", phenoB)

##assigning gsea()
gs_res = {} 
gs_res = gp.gsea(data=gene_exp, # or data='./data.txt'		
                 gene_sets=sys.argv[1],
                 cls= sys.argv[2],
                 # set permutation_type to phenotype if samples >=15
                 permutation_type='phenotype',
                 permutation_num=10, # reduce number to speed up test
                 outdir=None,  # do not write output to disk
                 method='signal_to_noise',
                 threads=4, seed= 7)

#access the dataframe results throught res2d attribute
gs_res.res2d.head()

#############################VISUALIZATIONS###########################

from gseapy import gseaplot, heatmap, dotplot, ringplot
terms = gs_res.res2d.Term
i = 2
# Make sure that ``ofname`` is not None, if you want to save your figure to disk
gseaplot(gs_res.ranking, term=terms[i], **gs_res.results[terms[i]])

# plotting heatmap
genes = gs_res.res2d.Lead_genes[i].split(";")
# Make sure that ``ofname`` is not None, if you want to save your figure to disk
heatmap(df = gs_res.heatmat.loc[genes], z_score=0, title=terms[i], figsize=(14,4), cmap=plt.cm.RdBu_r)
# to save your figure, make sure that ``ofname`` is not None
ax = dotplot(gs_res.res2d,
             column='log2 fold change',
             title='Gene Expression Difference',
             cmap=plt.cm.viridis,
             size=15,
             figsize=(4,5), cutoff=1)


