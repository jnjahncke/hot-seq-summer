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
    expr_dict = rnaseqs_to_dict(["RawData/HUMAN_genes.txt"])
  
    run_gsea(expr_dict["RawData/HUMAN_genes.txt"], "hsapiens", "human" )
    #run_gsea(expr_dict["RawData/mus_rna_seq_final.txt"],"mmusculus", )
    #run_gsea(expr_dict["RawData/yeast_degs.txt"],"scerevisiae" )
  
def run_gsea(expr_dict, species, common_name):
    gene_list = {}
    for gene in expr_dict:
        gene_list[gene] = float(expr_dict[gene][0])	###########################################fix line###################
    #glist = dict(sorted(gene_list.items(), reverse = True, key=lambda item: item[1])).keys()
    glist = sorted(gene_list, key = gene_list.get)
  
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
                      gene_sets=['GO_Cellular_Component_2021','GO_Molecular_Function_2021'],
                      organism=common_name, #set organism to the one you want (human, mouse, yeast)
                      outdir=None, #doesn't save the output to your machine               
                     )
    enr.results.to_csv(f'{species}_gsearesults.tsv', sep = '\t')    
    
    #plot enriched data sets
    barplot(enr.res2d,title='GO_Molecular_Function_2021', ofname='barplot.pdf')
    dotplot(enr.res2d,title='GO_Molecular_Function_2021', ofname='dotplot.png')
    
if __name__ == "__main__":
    main()
