#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import pandas as pd
import numpy as np
import numpy as np; import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


part_df = pd.read_csv ('resources/Atts_agroconcept_int.csv',index_col=False,header=0)
nonpart_df = pd.read_csv ('resources/Atts_nonpart_int.csv',index_col=False,header=0)

part_df = part_df[['CC_import','CC_import_change']].T

print('The cosine similarity for the two fields, CC_import and CC_import_change, is:','\n', cosine_similarity(part_df))


# In[2]:


nonpart_df = nonpart_df[['CC_import_nonpart','CC_import_change_nonpart']].T

print('The cosine similarity for the non participants, CC_import_nonpart and CC_import_change_nonpart, is:','\n', cosine_similarity(nonpart_df))


# In[3]:


part_df = pd.read_csv ('resources/Atts_agroconcept_int.csv',index_col=False,header=0)
nonpart_df = pd.read_csv ('resources/Atts_nonpart_int.csv',index_col=False,header=0)

part_df = part_df[['furt_reduc','CC_import','CC_import_change']].T

print('The cosine similarity for the participants across furt_reduc, CC_import and CC_import_change is:','\n', cosine_similarity(part_df))


# In[4]:



nonpart_df = pd.read_csv ('resources/Atts_nonpart_int.csv',index_col=False,header=0)

nonpart_df = nonpart_df[['furt_reduc_nonpart','CC_import_nonpart','CC_import_change_nonpart']].T

print('The cosine similarity for nonparticipants across furt_reduc_nonpart, CC_import_nonpart and CC_import_change_nonpart is:','\n', cosine_similarity(nonpart_df))


# In[ ]:




