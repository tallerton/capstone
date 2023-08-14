#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import pandas as pd
import numpy as np

import urllib
import json
import operator

import matplotlib as plot
import matplotlib.pyplot as plt
import seaborn as sn


# In[2]:


#load the data files
df_inf_part = pd.read_csv ('resources/influence_agroconcept.csv',index_col=False,header=0).dropna()
df_inf_nonpart = pd.read_csv ('resources/influence_nonagroconcept.csv',index_col=False,header=0).dropna()
frames =[df_inf_part , df_inf_nonpart]
df_combined = pd.concat(frames)

#node network
G3= nx.from_pandas_edgelist(df_combined, source='sender_id', target='receiver_id', edge_attr=["influence_x","influence_y"],create_using=nx.DiGraph()) 
nx.draw_random(G3,with_labels=True)
plt.show()

from decimal import *
node_max_degree = None  # the node which has the largest degree centrality value. This should be an integer. 
val_deg = None          # the centrality value of the node with the largest degree centrality. This should be a float. 

#calculate centrality
deg_dict = nx.degree_centrality(G3)
centrality_matrix = sorted(deg_dict.items(), key=lambda item:item[1],reverse=True)
maximum= centrality_matrix[0]
node_max_degree = maximum[0]
val_deg = maximum[1]


#calculate betweenness
bc = nx.betweenness_centrality(G3)
bc_dict = sorted(bc.items(), key=lambda item:item[1],reverse=True)#[-5:])
print('centrality: ',centrality_matrix)
print('\n--- ')
print('betweenness: ' ,bc_dict)


# In[ ]:




