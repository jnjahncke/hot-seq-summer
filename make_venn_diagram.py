#!/usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt 
from matplotlib_venn import venn3, venn3_circles
from matplotlib_venn import venn2, venn2_circles, venn2_unweighted


### Input: 3 species names, 3 separate lists an output file name and a title ###
### Output: a png file of a weighted venn diagram labeled with species names and a custom title ###


# Name list and title parameters
def make_venn_diagram(species1, species2, species3, list1, list2, list3, output_name, title):

  # Color scheme for venn circles
  colors = ['darkviolet','deepskyblue','blue']
  
  # Generate the diagram with passed in data
  venn_diagram = venn3([set(list1), set(list2), set(list3)], (species1, species2, species3), set_colors = colors)

  # Formatting
  plt.title(title)
  
  i = 0
  for text in venn_diagram.set_labels:
    text.set_fontweight('bold')
    text.set_fontsize(16)
    text.set_color(colors[i])
    i+=1

  for text in venn_diagram.subset_labels:
    text.set_color('white')
    text.set_fontsize(14)

  # Output venn diagram to a png image
  plt.savefig(f'{output_name}.png')



def main():

  species1 = sys.argv[1]
  species2 = sys.argv[2]
  species3 = sys.argv[3]

  list1 = sys.argv[4]
  list2 = sys.argv[5]
  list3 = sys.argv[6]

  output_name = sys.argv[7]
  title = sys.argv[8]

  make_venn_diagram(species1, species2, species3, list1, list2, list3, output_name, title)

if __name__ == '__main__':
  main()
