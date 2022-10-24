#!/usr/bin/env python3
###Gene set enrichment analysis KRL_10-24-22

import pandas as pd
from pandas import DataFrame as df
import gseapy as gp
from gseapy import gseaplot, heatmap, dotplot, ringplot
from gseapy.plot import barplot, dotplot
import matplotlib.pyplot as plt
import sys
import numpy as np
from gseapy import biomart
from shared_functions import *
    
def main():
    expr_dict = rnaseqs_to_dict(["RawData/HUMAN_gsea.txt","RawData/mus_rna_seq_final.txt", "RawData/yeast_degs.txt"])
  
    run_gsea(expr_dict["RawData/HUMAN_gsea.txt"], "hsapiens", "human" )
    run_gsea(expr_dict["RawData/mus_rna_seq_final.txt"],"mmusculus","mouse" )
    #run_gsea(expr_dict["RawData/yeast_degs.txt"],"scerevisiae", "Yeast")
  
def run_gsea(expr_dict, species, common_name):
    gene_list = {}
    for gene in expr_dict:
        gene_list[gene] = float(expr_dict[gene][0])	
    glist = sorted(gene_list, key = gene_list.get, reverse = True)
    
    #call species_annotation_df function and decalare species and ensemble data types
    x=species_annotation_df(species, 'external_gene_name')
  
    #create a dictonary that replaces glist ranked geneIDs with the appropriate entrez IDs
    ensembl2entrez = {}
    for gene in x:
        ensembl2entrez[gene]=x[gene][0]
    
    #convert gene names to gene symbols in previosuly ranked list
    elist = [] 
    for gene in glist:
        if gene in ensembl2entrez:
            elist.append(ensembl2entrez[gene])
    print(elist)
    
    #Run enrichr wrapper on new elist with declared gene set and species name
    enr = gp.enrichr(gene_list=elist, 
                      gene_sets=['GO_Molecular_Function_2021', 'GO_Biological_Process_2021', 'Pfam_Domains_2019'],
                      organism=common_name,
                      outdir=None, #doesn't save the output to your machine               
                     )
    enr.results.to_csv(f'{species}_gsearesults.tsv', sep = '\t')    
    
    #plot enriched data sets
    barplot(enr.res2d,title='Gene Set Enrichment Analysis', ofname=f'{common_name}_barplot.png')
    dotplot(enr.res2d,title='Gene Set Enrichment Analysis', ofname=f'{common_name}_dotplot.png')
    
if __name__ == "__main__":
    main()
