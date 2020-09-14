# -*- coding: utf-8 -*-
"""
Program Goals:
         This program is for extracting TKA constrain type 
         We already have an output of medtagger,
         which contains the list of found terms for TKA Constraint type and their evidences 
         
         This program applies some rules to create final output for TKA Constraint type data element
       
"""
################  Edit Section #############################
# put med_tagger output file name and its directory in the below line
med_tagger_file="../constraint/output/test/test.txt"
# put the name of directory that you want to see the output files 
output_path="../constraint/output/test/"

#######################################################  
# Libraries
def open_libraries():
    global pd, os, datetime,np, re
    import pandas as pd
    import os as os
    import datetime as datetime
    import numpy as np
    import re   as re



###################################   
def verify_consistency(table ,value):
        temp_document_level1=table[['MCN','doc_id',value]].drop_duplicates()
        temp_document_level2=temp_document_level1.groupby(['MCN','doc_id'])[value].count().reset_index()
        temp_document_level_issue=temp_document_level2[temp_document_level2[value]>1]['MCN'].unique().tolist()
        document_level_issue=pd.DataFrame()
        section_level_issue=pd.DataFrame()
        flag=0
        
        if len(temp_document_level_issue)==0:
               print("Perfect results")
               return(document_level_issue,section_level_issue, flag)
        else :   
                document_level_issue=temp_document_level1[temp_document_level1['MCN'].isin(temp_document_level_issue)  ]  
 
        document_level_issue2=pd.merge(table[['MCN','doc_id','section_name', 'covered_text','sentence', value]],document_level_issue,how='right', on=['MCN','doc_id', value])

        return(document_level_issue2, flag)  
####################################        
def prepare_doc_and_sentence_level_results(table):
             
             table_sentence_level=table[['MCN','doc_name', 'note_date','covered_text', 'norm_term',  
                                           'status', 'term_status', 'section_name',  'sentence',   'sent_id', 
                                           'doc_id',  'note_date','norm_term1']]
           
            
             #####################################
             #concatinate the found sentences and add the 
             table['evidence']= table['doc_name']+"::"+table['status']+"::"+table['covered_text'].astype(str)+"::"+table["norm_term1"]+"::"+table["section_name"]+"::"+table["sentence"]+"~~"
             table_sentence=table[['doc_id','evidence','norm_term']].groupby(['doc_id','norm_term'])['evidence'].sum().reset_index()
             doc_list=table[['MCN','doc_id','note_date']].drop_duplicates()
             
             table_doc_level=pd.merge(doc_list , table_sentence, how="left", on="doc_id")
             
             ##################################
             return(table_doc_level, table_sentence_level)             
#################################
# Main program block
if __name__=='__main__':     
                
             # open libraries     
             open_libraries()
             
                   
          
            
             # Read medtagger results from medtagger
             med_tagger=pd.read_csv(med_tagger_file,sep="|",  header=None, engine='python')
             len(med_tagger)
           
            
             
             med_tagger.columns=['doc_name','covered_text','norm_term','section_id','status','term_status',
                                 'experiencer','section_name','sentence','sent_id','begin','end']
            
        
             med_tagger['MCN']=med_tagger['doc_name'].str.slice(0,8)
             med_tagger['doc_id']= med_tagger['doc_name'].str.slice(9,16)
             med_tagger['note_date']= med_tagger['doc_name'].str.slice(-14,-4)
             med_tagger['norm_term1']=med_tagger['norm_term']
             
       
             print(med_tagger['MCN'].nunique())
            
             # to see which section we have in our results
             a=med_tagger[['section_name']].drop_duplicates()
             
             # Prepare sentence level results
             results_sentence_level=med_tagger[['MCN','doc_name', 'doc_id','note_date', 'covered_text', 'sentence','norm_term','status','term_status','section_name','sent_id','norm_term1']].drop_duplicates().sort_values(by="MCN")
             len(results_sentence_level)
            
             print(len(med_tagger))
           
             med_tagger=results_sentence_level
             a=verify_consistency(med_tagger, 'norm_term')
             print(med_tagger.groupby('norm_term')['MCN'].count().reset_index())
     
             #######################################
#              Prioritize ccks
             cck=med_tagger[(med_tagger['norm_term']=='CCK')  ]
             print(len(cck))
             
             
             med_tagger.loc[med_tagger['doc_id'].isin(cck['doc_id'].unique().tolist()),'norm_term']='CCK'
             print(med_tagger.groupby('norm_term')['MCN'].count().reset_index())
             
#             ###############################

             # Prioritize decision based on "implanct name" and "Implant Placement" sections result 
             
             def implant_name_priority(norm_term):
                  print(norm_term)
                  temp=med_tagger[(med_tagger['norm_term']==norm_term) & (med_tagger['section_name'].isin(['Implant Name'])) ]
                  med_tagger.loc[med_tagger['doc_id'].isin(temp['doc_id'].unique().tolist()),'norm_term']=norm_term
                  print(med_tagger.groupby('norm_term')['MCN'].count().reset_index())
             def implant_name_priority2(norm_term):
                  print(norm_term)
                  temp=med_tagger[(med_tagger['norm_term']==norm_term) & (med_tagger['section_name'].isin(['Implant Placement'])) ]
                  med_tagger.loc[med_tagger['doc_id'].isin(temp['doc_id'].unique().tolist()),'norm_term']=norm_term
                  print(med_tagger.groupby('norm_term')['MCN'].count().reset_index())
              
              #######################################
             # Prioritize based on this order CCK, MC, UC, CR, PS#                
       
             for norm_term in ['CCK','MC','UC','CR','PS']:
                implant_name_priority(norm_term)
            
             for norm_term in ['CCK','MC','UC','CR','PS']:
                implant_name_priority2(norm_term)
                    
                
             # Prioritize CR
             CR=med_tagger[med_tagger['norm_term']=='CR']
             print(len(CR))
         
             med_tagger.loc[med_tagger['doc_id'].isin(CR['doc_id'].unique().tolist()),'norm_term']='CR'
             CR=med_tagger[med_tagger['norm_term']=='CR']
             print(len(CR))
             
             ##################################           
             document_level_issue=verify_consistency(med_tagger,'norm_term')
             doc_level,sent_level=prepare_doc_and_sentence_level_results(med_tagger)
             
           
             
             # save the ouput
             doc_level.to_excel(output_path+"doc_level.xlsx", index=False)
             sent_level.to_excel(output_path+"sent_level.xlsx", index=False)
             print(len(doc_level))
    
     
     
     
