#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import pandas as pd
import numpy as np

import urllib
import json
import operator

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#import seaborn as sns


# In[5]:


import pandas as pd
df = pd.read_csv ('resources/Atts_agroconcept_survey.csv',index_col=False,header=0)
df_edges = pd.read_csv ('resources/Edges_complete.csv',index_col=False,header=0)
df_raw = pd.read_csv ('resources/rawdata_new.csv',index_col=False,header=0)
#get list of nodes in network name1
nodes_in_name1=[]
nodes_with_edges=[]
nodes_with_edges = df_edges['sender_id'].unique().tolist()

df_raw = df_raw[~df_raw['id'].isin(nodes_with_edges)]
for i in df.index:
    if df['net_name1_neigh'][i] == 1 or df['net_name1_work'][i] == 1 or df['net_name1_frien'][i] == 1 or df['net_name1_fam'][i] == 1 or df['net_name1_part'][i] == 1 or df['net_name1_club'][i] == 1  or df['net_name1_vet'][i] == 1 or df['net_name1_ext'][i] == 1 or df['net_name1_oth'][i] == 1 :
        nodes_in_name1.append(df['ego_id'][i])

G = nx.from_pandas_edgelist(df_edges, source='sender_id', target='receiver_id', edge_attr=["advice_freq"],create_using=nx.DiGraph())
#G.add_nodes_from(df_raw['id'].values)
#plt.figure(1, figsize=(50, 50),dpi=50)
nx.draw_random(G, with_labels=True, node_size=400)
#plt.show()
#G.add_nodes_from(nodes_in_name1)
#nx.draw(G,with_labels=True)
#G = nx.from_pandas_edgelist(df,'ego_id')
#print(df)


# In[15]:


node_max_degree = None  # the node which has the largest degree centrality value. This should be an integer. 
val_deg = None          # the centrality value of the node with the largest degree centrality. This should be a float. 

deg_dict = nx.degree_centrality(G)
max= sorted(deg_dict.items(), key=lambda item:item[1],reverse=True)[0]
node_max_degree = max[0]
val_deg = max[1]
print('The node which has the largest degree centrality value is node #',node_max_degree,)
print('And the centrality value is',val_deg)


# In[18]:


max_5_cc = []  # a list of 5 nodes with the largest closeness centrality values
min_5_cc = []  # a list of 5 nodes with the smallest closeness centrality values
# YOUR CODE HERE
cc = nx.closeness_centrality(G)
cc_dict = sorted(cc.items(), key=lambda item:item[1],reverse=True)#[-5:])
max_5_cc = [x[0] for x in cc_dict[:5]] # use list comprehension to get node only
min_5_cc = [x[0] for x in cc_dict[-5:]] # use list comprehension to get node only
print('The 5 nodes with the largest closeness centrality values are', max_5_cc)
print('The 5 nodes with the smallest closeness centrality values are', min_5_cc)


# In[19]:


max_5_bc = []  # a list of 5 nodes with the largest betweenness centrality values
min_5_bc = []  # a list of 5 nodes with the smallest betweenness centrality values

# YOUR CODE HERE
bc = nx.betweenness_centrality(G)
bc_dict = sorted(bc.items(), key=lambda item:item[1],reverse=True)#[-5:])
max_5_bc = [x[0] for x in bc_dict[:5]] # use list comprehension to get top 5 nodes only
min_5_bc = [x[0] for x in bc_dict[-5:]] # use list comprehension to get bottom 5 nodes only
print(max_5_bc, min_5_bc)


# In[20]:


graph_trans = None      # graph transitivity. This should be a float. 
avg_clustering = None   # average clustering coefficient value. This should be a float. 

# YOUR CODE HERE
graph_trans = nx.transitivity(G)
avg_clustering = nx.average_clustering(G)
print(graph_trans,avg_clustering)


# In[ ]:





# In[ ]:




