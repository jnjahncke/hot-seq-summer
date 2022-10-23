#!/usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt 
from matplotlib_venn import venn3, venn3_circles
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted
from shared_functions import *


### Input: three sets of lists one for each species ###
### Output: a png file with a venn diagram labeled with the comparison type and species names ###



species1 = 'H. sapiens'
species2 = 'M. musculus'
species3 = 'S. cerevisiae'

list1 = [3,5,6,7,4,7,5,3,7,7,8,8,7,3,9,4]
list2 = [3,67,35,24,6,8,9,4,7,9,3,0,34,3]
list3 = [4,6,4,67,86,23,56,7,8,9,65,32,4]



# Name list parameters
def make_venn_diagram():

  # Convert to a set in the venn function
  venn_diagram = venn3([set(list1), set(list2), set(list3)], ('species1', 'species2', 'species3'))

  # Color scheme for venn circles
  colors = ['darkviolet','deepskyblue','blue']

  # Generate the diagram with passed in data
  vennPlot = venn3([set(list1), set(list2), set(list3)], 
                 (f'$\it{species1}$', '$\it{species2}$', '$\it{species3}$'), 
                 set_colors = colors)


  # Formatting
  plt.title(f"Shared {analysis} differentially observed under heat stress")

  i = 0
  for text in vennPlot.set_labels:
    text.set_fontweight('bold')
    text.set_fontsize(16)
    text.set_color(colors[i])
    i+=1

  for text in vennPlot.subset_labels:
    text.set_color('white')
    text.set_fontsize(14)

  plt.figure(figsize=(7,7))
  plt.show(vennPlot)  



  # Output venn diagram to a png image
  plt.savefig(f'{venn_output}.png', bbox_inches='tight')



#def main()

#if __name__ == '__main__':
  #main()
