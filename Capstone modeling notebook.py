#!/usr/bin/env python
# coding: utf-8

# In[39]:


import networkx as nx
import pandas as pd
import numpy as np

import urllib
import json
import operator

import matplotlib as plot
import matplotlib.pyplot as plt
import seaborn as sn
#import seaborn as sns


# In[ ]:





# In[40]:


import pandas as pd
df = pd.read_csv ('resources/Atts_agroconcept_survey.csv',index_col=False,header=0)
df_edges = pd.read_csv ('resources/Edges_complete.csv',index_col=False,header=0)
#create a new column ccmm_score that averages all of the self_* columns
df['ccmm_score']= (df['self_reduc']+df['self_act']+df['self_cap']+df['self_conf']+df['self_not'])/5
#print(df['ego_id'],df['ccmm_score'])
df_raw = pd.read_csv ('resources/rawdata_new.csv',index_col=False,header=0)
#get list of nodes in network name1
nodes_in_name1=[]
nodes_with_edges=[]
nodes_with_edges = df_edges['sender_id'].unique().tolist()
#calculate measured mitigation
farmtype = df['farmtype'].unique().tolist()
print(farmtype)
df['mitigation_measure']=0
for i in df.index:
    mm_total=0
    if df['legum'][i] == 1 :
        mm_total+=1
    if df['conc'][i] == 1 :
        mm_total+=1
    if df['add'][i] == 1 :
        mm_total+=1
    if df['lact'][i] == 1 :
        mm_total+=1
    if df['breed'][i] == 1 :
        mm_total+=1
    if df['covman'][i] == 1 :
        mm_total+=1
    if df['comp'][i] == 1 :
        mm_total+=1
    if df['drag'][i] == 1 :
        mm_total+=1
    if df['cov'][i] == 1 :
        mm_total+=1
    if df['plough'][i] == 1 :
        mm_total+=1
    if df['solar'][i] == 1 :
        mm_total+=1
    if df['biog'][i] == 1 :
        mm_total+=1
    if df['ecodr'][i] == 1 :
        mm_total+=1
    df['mitigation_measure'][i] = mm_total/13
print(df['mitigation_measure'] )
print("mean ",df['mitigation_measure'].mean())
df_raw = df_raw[~df_raw['id'].isin(nodes_with_edges)]
for i in df.index:
    if df['net_name1_neigh'][i] == 1 or df['net_name1_work'][i] == 1 or df['net_name1_frien'][i] == 1 or df['net_name1_fam'][i] == 1 or df['net_name1_part'][i] == 1 or df['net_name1_club'][i] == 1  or df['net_name1_vet'][i] == 1 or df['net_name1_ext'][i] == 1 or df['net_name1_oth'][i] == 1 :
        nodes_in_name1.append(df['ego_id'][i])

G = nx.from_pandas_edgelist(df_edges, source='sender_id', target='receiver_id', edge_attr=["advice_freq"],create_using=nx.DiGraph())
#G.add_nodes_from(df_raw['id'].values)
#plt.figure(1, figsize=(50, 50),dpi=50)
#nx.draw_random(G, with_labels=True, node_size=400)
#plt.show()
#G.add_nodes_from(nodes_in_name1)
#nx.draw(G,with_labels=True)
#G = nx.from_pandas_edgelist(df,'ego_id')
#print(df)

plt.figure(3,figsize=(12,12)) 
nx.draw_random(G,with_labels=True)
plt.show()


# In[55]:


# plotting the heatmap
linewidths = .11
linecolor = "blue"

sn.heatmap(data=df[['reducpercent','co22015', 'co22018']],
                linewidths=linewidths,
                linecolor=linecolor, annot=False)
#plt.gcf().set_size_inches(15, 10)
#plt.show()


# In[42]:


from decimal import *
node_max_degree = None  # the node which has the largest degree centrality value. This should be an integer. 
val_deg = None          # the centrality value of the node with the largest degree centrality. This should be a float. 

deg_dict = nx.degree_centrality(G)
centrality_matrix = sorted(deg_dict.items(), key=lambda item:item[1],reverse=True)
maximum= centrality_matrix[0]
node_max_degree = maximum[0]
val_deg = maximum[1]

#print('The node which has the largest degree centrality value is node #',node_max_degree,)
#print('And the centrality value is',val_deg)

#calculate betweenness
bc = nx.betweenness_centrality(G)
bc_dict = sorted(bc.items(), key=lambda item:item[1],reverse=True)#[-5:])
#print('centrality: ',centrality_matrix)
#print('betweenness: ' ,bc_dict)


# In[43]:


x=[]
x_nodes=[]
y=[]
for entry in centrality_matrix:
    if entry[0] in nodes_with_edges:
        x.append(entry[1])
        x_nodes.append(entry[0])
# x=np.array(list(zip(*centrality_matrix))[1])
# x_nodes=list(zip(*centrality_matrix))[0]

for node in x_nodes:
    if node in nodes_with_edges:
        y.append(df[df['ego_id']==node]['ccmm_score'].values[0])

#print('length of x is ',len(x),'\n')
#print('the CCMM scores, which is x, are = ',x,'\n')
#print('x_nodes, the nodes with highest centrality go in order as ',x_nodes,'\n')
#print('length of y is ',len(y),'\n')
#print(y)
plt.figure(figsize=(16,9))
line=plt.bar(x_nodes,y, width=1)
plt.xlabel('Individual Node Number')
plt.ylabel('Aggregated Perceived CCMM Score')

for i in range(len(x)):
    plt.annotate(str(x_nodes[i]), xy=(x_nodes[i],y[i]), ha='center', va='bottom')

plt.title('Farm Nodes and CCMM Scores', fontsize=16)
plt.show()


# In[44]:


x=[]
x_nodes=[]
y=[]
for entry in centrality_matrix:
    if entry[0] in nodes_with_edges:
        x.append(entry[1])
        x_nodes.append(entry[0])

for node in x_nodes:
    if node in nodes_with_edges:
        y.append(df[df['ego_id']==node]['mitigation_measure'].values[0])

plt.figure(figsize=(16,9))
line=plt.bar(x_nodes,y, width=1)
plt.xlabel('Individual Node Number')
plt.ylabel('Mitigation measure')

for i in range(len(x)):
    plt.annotate(str(x_nodes[i]), xy=(x_nodes[i],y[i]), ha='center', va='bottom')

plt.title('Farm Nodes and Mitigation Measures', fontsize=16)
plt.show()


# In[45]:


#maybe plot the bars in order, from highest centrality to last

x=[]
x_nodes=[]
y=[]
for entry in centrality_matrix:
    if entry[0] in nodes_with_edges:
        x.append(entry[1])
        x_nodes.append(entry[0])

for node in x_nodes:
    if node in nodes_with_edges:
        y.append(df[df['ego_id']==node]['co22018'].values[0])

plt.figure(figsize=(16,9))
line=plt.bar(x_nodes,y, width=1)
plt.xlabel('Individual Node Number')
plt.ylabel('co22018')

for i in range(len(x)):
    plt.annotate(str(x_nodes[i]), xy=(x_nodes[i],y[i]), ha='center', va='bottom')


plt.show()


# In[46]:


max_5_cc = []  # a list of 5 nodes with the largest closeness centrality values
min_5_cc = []  # a list of 5 nodes with the smallest closeness centrality values
# YOUR CODE HERE
cc = nx.closeness_centrality(G)
cc_dict = sorted(cc.items(), key=lambda item:item[1],reverse=True)#[-5:])
max_5_cc = [x[0] for x in cc_dict[:5]] # use list comprehension to get node only
min_5_cc = [x[0] for x in cc_dict[-5:]] # use list comprehension to get node only
print('The 5 nodes with the largest closeness centrality values are', max_5_cc)
print('The 5 nodes with the smallest closeness centrality values are', min_5_cc)


# In[47]:


max_5_bc = []  # a list of 5 nodes with the largest betweenness centrality values
min_5_bc = []  # a list of 5 nodes with the smallest betweenness centrality values

# YOUR CODE HERE
bc = nx.betweenness_centrality(G)
bc_dict = sorted(bc.items(), key=lambda item:item[1],reverse=True)#[-5:])
max_5_bc = [x[0] for x in bc_dict[:5]] # use list comprehension to get top 5 nodes only
min_5_bc = [x[0] for x in bc_dict[-5:]] # use list comprehension to get bottom 5 nodes only
print(max_5_bc, min_5_bc)


# In[48]:


graph_trans = None      # graph transitivity. This should be a float. 
avg_clustering = None   # average clustering coefficient value. This should be a float. 

# YOUR CODE HERE
graph_trans = nx.transitivity(G)
avg_clustering = nx.average_clustering(G)
print(graph_trans,avg_clustering)


# In[ ]:





# In[49]:


x=[]
x_nodes=[]
y=[]
for entry in centrality_matrix:
    if entry[0] in nodes_with_edges:
        y.append(entry[1])
        x_nodes.append(entry[0])

#plt.subplot(1,2,1)
line=plt.bar(x_nodes,y, width=1)
plt.xlabel('Individual Node Number')
plt.ylabel('Centrality')
plt.figure(figsize=(12,12))
for i in range(len(x_nodes)):
    plt.annotate(str(x_nodes[i]), xy=(x_nodes[i],y[i]), ha='center', va='bottom')
plt.show()
#plot nodes with reducpercent
y2=[]
#plt.subplot(1,2,2)
for node in x_nodes:
    if node in nodes_with_edges:
        y2.append(-(df[df['ego_id']==node]['reducpercent'].values[0]))

line=plt.bar(x_nodes,y2, width=1)
plt.xlabel('Individual Node Number')
plt.ylabel('Percent reduction in CO2')
plt.figure(figsize=(12,12))
for i in range(len(x_nodes)):
    plt.annotate(str(x_nodes[i]), xy=(x_nodes[i],y[i]), ha='center', va='bottom')

#plt.tight_layout()
plt.show()


# In[50]:


import matplotlib.pyplot as plt

#x=[]
x_nodes=[]
y=[]
for entry in centrality_matrix:
    if entry[0] in nodes_with_edges:
        y.append(entry[1])
        x_nodes.append(entry[0])
fig,ax= plt.subplots(1,1)

#plt.figure(figsize=(16,9))
ax.bar(x_nodes,y, width=1)
ax.set_title('Centrality scores')
ax.set_ylabel('Centrality')
ax.get_xaxis().set_visible(False)

for i in range(len(x)):
    ax.annotate(str(x_nodes[i]), xy=(x_nodes[i],y[i]), ha='center', va='bottom')


plt.show()


# In[51]:


['mainprodcution','reducpercent']

df = pd.read_csv ('resources/Atts_agroconcept_survey.csv',index_col=False,header=0)
df3 = pd.DataFrame(df, columns=['mainprodcution','reducpercent'])
#

field = "mainprodcution"
sort_order = ["arable", "cattle", "dairy", "suckler", "wine", "vegetables"]
ax = df3.set_index(field).loc[sort_order].plot(kind="bar", legend=False, figsize=(19,10))
ax.set_xlabel("Main Production", fontsize=16)
ax.set_ylabel("CO2 Percent Reduction", fontsize=16)
ax.set_title('Net Reduction in CO2 by Production Type', fontsize=16)
plt.xticks(rotation = 45, fontsize=14)
plt.yticks(fontsize=14)
#plt.xticks()


plt.show()


# In[52]:


df = pd.read_csv ('resources/Atts_agroconcept_survey.csv',index_col=False,header=0)
df4 = pd.DataFrame(df, columns=['interviewtime','reducpercent'])
#
fig1, ax1 = plt.subplots(figsize=(18,10))
ax1.set_title('How long the participant took to answer the whole survey', fontsize=16)
ax1.bar(np.arange(len(df)), df['reducpercent'])
ax1.set_xticks(np.arange(len(df)))
ax1.set_xticklabels(df['interviewtime'])
ax.set_xlabel("Duration of Interview (s)", fontsize=16)
ax.set_ylabel("CO2 Percent Reduction", fontsize=16)
plt.xticks(rotation = 45, fontsize=14)
plt.yticks(fontsize=14)

plt.show()


# In[53]:


#get the nodes(farms) with more than 5 networks
impactful_farms=[]
impactful_co2_reduction=[]
for i in df.index:
    if df['network'][i] >= 6 :
        impactful_farms.append(df['ego_id'][i])

#print(impactful_farms)
for farm in impactful_farms:
    #print(df[df['ego_id']==farm])
    impactful_co2_reduction.append(df[df['ego_id']==farm]['reducpercent'].values[0])
#print(impactful_co2_reduction)

plt.figure(figsize=(16,8))
plt.bar(impactful_farms,impactful_co2_reduction)

plt.xlabel('Farm Node Number')
plt.ylabel('Percent reduction in CO2')
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("", fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)


for i in range(len(impactful_farms)):
    plt.annotate(str(impactful_farms[i]), xy=(impactful_farms[i],impactful_co2_reduction[i]), ha='center', va='bottom')
    
plt.title('Impactful Farms and Net Reduction of CO2', fontsize=16)


# In[ ]:




