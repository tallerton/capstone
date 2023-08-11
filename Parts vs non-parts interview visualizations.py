#!/usr/bin/env python
# coding: utf-8

# In[1]:


import altair as alt
import pandas as pd


part_df = pd.read_csv ('resources/Atts_agroconcept_int.csv',index_col=False,header=0)
nonpart_df = pd.read_csv ('resources/Atts_nonpart_int.csv',index_col=False,header=0)

#add a field to represents participant/nonparticipant to both dataframes for Altairs legend
part_df['Conference participant']='Yes'
nonpart_df['Conference participant']='No'
part_df['mean'] = part_df['CC_import_change'].mean()
nonpart_df['mean'] = nonpart_df['CC_import_change_nonpart'].mean()

#the fields they share are = 'ego_id', 'CC_import_change' ('CC_import_change_nonpart'), 'furt_reduc' ('furt_reduc_nonpart'), 'CC_import' ('CC_import_nonpart')
chart1 = alt.Chart(part_df,title="How important is climate change mitigation for your decisions on the farm today compared to 10 years ago?").encode(
        y=alt.Y('CC_import_change',title="Importance"),
        x=alt.X('ego_id:N',title='Farm ID',axis=alt.Axis(labels=False)),
        text='ego_id'
        
)


bars = chart1.mark_bar().encode(color='Conference participant')
text = chart1.mark_text(align='center',fontWeight='bold',dy=-6)
rule = alt.Chart(part_df).mark_rule(strokeWidth=.2).encode(y='mean:Q',color='Conference participant'
)
chart2 = alt.Chart(nonpart_df,title="How important is climate change mitigation for your decisions on the farm today compared to 10 years ago?").encode(
        y=alt.Y('CC_import_change_nonpart',title="Importance"),
        x=alt.X('ego_id_nonpart:N',title='Farm ID',axis=alt.Axis(labels=False)),
      
        text='ego_id_nonpart'
        )

bars2=chart2.mark_bar().encode(color='Conference participant')
text2 = chart2.mark_text(align='center',dy=-6,fontWeight='bold')
rule2 = alt.Chart(nonpart_df).mark_rule(color='purple',strokeWidth=.2).encode(y='mean:Q',color='Conference participant')
text5 = (
    alt.Chart(part_df)
    .mark_text(text=['Gold line represents the mean for attendees', 'Blue line represents the mean for non-attendees'],fontWeight='normal', x='width', y='height', dx = 10, dy=40)
  
)


(bars + bars2 + text5 +text2+rule + rule2+text).properties(
    width=800,
    height=350,
    
)


# In[2]:


part_df['mean'] = part_df['furt_reduc'].mean()
nonpart_df['mean'] = nonpart_df['furt_reduc_nonpart'].mean()


chart1 = alt.Chart(part_df,title="Do you consider to implement further mitigation measures on your farm?").encode(
        y=alt.Y('furt_reduc',title=["Binary response:",' ', "0=No, 1=Yes, 2=Maybe"], axis=alt.Axis(tickMinStep=1,labelAngle=0)),
        x=alt.X('ego_id:N',title='Farm ID',axis=alt.Axis(labels=False)),
        
        text='ego_id'
        )
bars = chart1.mark_bar().encode(color='Conference participant')

rule = alt.Chart(part_df).mark_rule().encode(y='mean:Q',color='Conference participant')
chart2 = alt.Chart(nonpart_df,title="Do you consider to implement further mitigation measures on your farm?").encode(
        y=alt.Y('furt_reduc_nonpart',title=["Binary response:",' ', "0=No, 1=Yes, 2=Maybe"], axis=alt.Axis(tickMinStep=1,labelAngle=0)),
        x=alt.X('ego_id_nonpart:N',title='Farm ID',axis=alt.Axis(labels=False)),
        
        text='ego_id_nonpart'
        )


bars2=chart2.mark_bar().encode(color='Conference participant')

rule2 = alt.Chart(nonpart_df).mark_rule().encode(y='mean:Q',color='Conference participant')
text5 = (
    alt.Chart(part_df)
    .mark_text(text=['Gold line represents the mean for attendees', 'Blue line represents the mean for non-attendees'],fontWeight='normal', x='width', y='height', dx = 10, dy=40)
  
)

text = chart1.mark_text(align='center',fontWeight='bold',dy=-6)
text2 = chart2.mark_text(align='center',dy=-6,fontWeight='bold')
#((bars + text + rule)  + (bars2 + text2) ).properties(
(bars + bars2 +text + text2 + rule + rule2+text5).properties(
    width=750,
    height=350,
    

).configure_axis(
    labelFontWeight=100,
    labelFontSize=10,
    titleFontSize=12
)


# In[3]:


part_df['mean'] = part_df['CC_import'].mean()
nonpart_df['mean'] = nonpart_df['CC_import_nonpart'].mean()


chart1 = alt.Chart(part_df,title="How important is climate change mitigation for your decisions on the farm?").encode(
        y=alt.Y('CC_import',title="Importance, Average Importance"),
        x=alt.X('ego_id:N',title='Farm ID',axis=alt.Axis(labels=False)),
        
        text='ego_id'
        )

bars = chart1.mark_bar().encode(color='Conference participant')
text = chart1.mark_text(align='center',fontWeight='bold',dy=-6)
rule = alt.Chart(part_df).mark_rule().encode(y='mean:Q',color='Conference participant')
chart2 = alt.Chart(nonpart_df,title="How important is climate change mitigation for your decisions on the farm?").encode(
        y=alt.Y('CC_import_nonpart',title="Importance, Average Importance"),
        x=alt.X('ego_id_nonpart:N',title='Farm ID',axis=alt.Axis(labels=False)),
        
        text='ego_id_nonpart'
        )

bars2=chart2.mark_bar().encode(color='Conference participant')
text2 = chart2.mark_text(align='center',dy=-6,fontWeight='bold')
rule2 = alt.Chart(nonpart_df).mark_rule(color='purple').encode(y='mean:Q',color='Conference participant')

text5 = (
    alt.Chart(part_df)
    .mark_text(text=['Gold line represents the mean for attendees', 'Blue line represents the mean for non-attendees'],fontWeight='normal', x='width', y='height', dx = 10, dy=40)
    
)


(bars + bars2 +text + text2 + rule + rule2+text5).properties(
    width=800,
    height=350,
    
)


# In[ ]:




