# hot-seq-summer

### Datasets:

* Mus musculus: `mus_rna_seq.py` takes in `mus_rnaseq_data.xlsx` (from [this paper](https://elifesciences.org/articles/07687/)) and returns `mus_rna_seq_final.txt` - a tab delimited file containing three columns: ensembl accession ID, log fold change, and p-value.


### Getting domains/GO terms:

* `annotation_download.py` can write domains (from pfam) or GO terms (from Ensembl) to .txt file
