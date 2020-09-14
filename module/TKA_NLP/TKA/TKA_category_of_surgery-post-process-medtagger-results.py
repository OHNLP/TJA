# -*- coding: utf-8 -*-
""" 
Program Goals:
         This progrma is to prepare output for TKA_category of surgery
         We have already an output from medtagger,
         which contains the list of found terms for TKA_category of surgery and their evidences 
         
         This program applies some rules to create final output for the TKA_category of surgery data element
"""
################  Edit Section #############################
# put med_tagger output results and its directory in the below line
med_tagger_file="../type_of_surgery/output/test/test.xlsx"

# put the name of directory that you want to see the output files 

output_path="../type_of_surgery/output/test/"

#######################################################  

###########################################    

# Libraries
def open_libraries():
    global pd, os, datetime,np, re
    import pandas as pd
    import os as os
    import datetime as datetime
    import numpy as np
    import re   as re

##########################################
  

###################################   
def verify_consistency(table ,value):
         # Find document level issues : if there are two different values for a patient on one document
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
 
###############################
def prepare_doc_and_sentence_level_results(table):
             table=med_tagger
             table_sentence_level=table[['MCN','doc_name', 'note_date','covered_text', 'norm_term', 'section_id', 
                                           'status', 'term_status','experiencer', 'section_name',  'sentence',   'sent_id', 'begin', 'end',
                                           'doc_id',  'note_date']]
           
            
             #####################################
             #concatinate the found sentences and add the 
             table['evidence']= table['doc_name']+"::"+table['status']+"::"+table['section_id'].astype(str)+"::"+table["section_name"]+"::"+table["sentence"]+"~~"
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
             med_tagger=pd.read_excel(med_tagger_file,  header=None)
             len(med_tagger)
                  
           
            
             
             med_tagger.columns=['doc_name','covered_text','norm_term','section_id','status','term_status',
                                 'experiencer','section_name','sentence','sent_id','begin','end']
            
        
             med_tagger['MCN']=med_tagger['doc_name'].str.slice(0,8)
             med_tagger['doc_id']= med_tagger['doc_name'].str.slice(9,16)
             med_tagger['note_date']= med_tagger['doc_name'].str.slice(-14,-4)
             
       
             print(med_tagger['MCN'].nunique())
             
             
             a=med_tagger[['section_name']].drop_duplicates()
             
             results_sentence_level=med_tagger[['MCN','doc_name', 'doc_id','note_date', 'covered_text', 'sentence','norm_term','status','term_status','section_name','sent_id']].drop_duplicates().sort_values(by="MCN")
             len(results_sentence_level)
            
             
               
             
             document_level_issue, flag=verify_consistency(results_sentence_level,'norm_term')
             doc_level,sent_level=prepare_doc_and_sentence_level_results(med_tagger)
             
             # save the ouput
             doc_level.to_excel(output_path+"doc_level.xlsx", index=False)
             sent_level.to_excel(output_path+"sent_level.xlsx", index=False)
             
             
        
     
     
     
     
     
     
