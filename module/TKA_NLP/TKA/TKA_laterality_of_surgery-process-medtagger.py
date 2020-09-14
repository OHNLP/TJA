
"""
 
Program Goals:
         This program is for extracting TKA_laterality of surgery
         We have already an output from medtagger,
         which contains the list of found terms for TKA_laterality of surgery and their evidence 
         
         This program applies some rules to create final output for the TKA_laterality of surgery data element
"""
################  Edit Section #############################
# put med_tagger output results and its directory in the below line
med_tagger_file="../output/test/test.txt"

# put the name of directory that you want to see the output files 

output_path="../output/test/"

###################################
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
def prepare_results(table):
             sent_level=table.reset_index(drop=True)
             document_level_issue, flag=verify_consistency(sent_level,'norm_term')
             # for those with both left and righ norm terms we will change it to both
             sent_level.loc[sent_level['doc_id'].isin(document_level_issue['doc_id'].tolist()),'norm_term']='BOTH'
             

              
             # Prepare document level resuls
             sent_level['sentence']= "~~"+sent_level['doc_name']+"::"+sent_level['section_name']+"::"+sent_level['sentence']
             sent_level_temp=sent_level.groupby(['doc_id'])['sentence'].sum().reset_index()
             len(sent_level_temp['doc_id'].unique())
             
             results_doc_level=pd.merge(sent_level[['MCN','doc_id',"note_date","norm_term"]], sent_level_temp, how="left", on="doc_id").drop_duplicates()
             a=len(results_doc_level)                 

            
             results_doc_level['sentence']= results_doc_level['sentence'].str.lstrip('~~')
             b=len(results_doc_level)
                
             if (a!=b):
                      print("*****************************************")
                      print("Error: something went wrong on adding sentences togethere")
                      print("*****************************************")
             return(sent_level,results_doc_level)         
                 
#        
#################################
# Main program block
def main():
     
                
             # open libraries     
            
             open_libraries()
             
             version = str(datetime.datetime.now())[0:19].replace(' ','-').replace(':','')
             print(version)    
        
          
            
             # Read medtagger results from medtagger
             med_tagger=pd.read_csv(med_tagger_file, sep="|", header=None)
             len(med_tagger)
            
            
           
            
             
             med_tagger.columns=['doc_name','covered_text','norm_term','section_id','status','term_status',
                                 'experiencer','section_name','sentence','sent_id','begin','end']
            
        
             
             med_tagger['split']= med_tagger['doc_name'].str.split('_')
             med_tagger[['MCN','doc_id','version','dep','dep2','note_date']]= pd.DataFrame(med_tagger.split.values.tolist(), index=med_tagger.index)
             
             med_tagger['sent_id']=med_tagger['sent_id'].str.replace(".*:","")
             print(med_tagger['MCN'].nunique())
             
             
             a=med_tagger[['section_name']].drop_duplicates()
             # keep just mentions on procedure section
             results_sentence_level=med_tagger[med_tagger['section_name']=='SERGURY_PROCEDURE'][['MCN','doc_name', 'doc_id','note_date', 'covered_text', 'sentence','norm_term','status','term_status','section_name','sent_id']].drop_duplicates().sort_values(by="MCN")
             postop_dx=med_tagger[med_tagger['section_name']=='SERGURY_POST_OPERATION_dx'][['MCN','doc_name', 'doc_id','note_date', 'covered_text', 'sentence','norm_term','status','term_status','section_name','sent_id']].drop_duplicates().sort_values(by="MCN")
             len(results_sentence_level)
          
            
             results_sentence_level=results_sentence_level.reset_index(drop=True)     
             results_sent_level2=results_sentence_level.copy()
             document_level_issue, flag=verify_consistency(results_sent_level2,'norm_term')
             
             # for those with both left and righ norm terms we will change it to both
             results_sent_level2.loc[results_sent_level2['doc_id'].isin(document_level_issue['doc_id'].tolist()),'norm_term']='BOTH'
             
             results_sent_level2.to_excel(output_path+"tka_results_sentence_level_"+version+".xlsx",index=False)
             
              
             # Prepare document level resuls
             results_sent_level2['sentence']= "~~"+results_sent_level2['doc_name']+"::"+results_sent_level2['section_name']+"::"+results_sent_level2['sentence']
             results_sentence_level_temp=results_sent_level2.groupby(['doc_id'])['sentence'].sum().reset_index()
             len(results_sentence_level_temp['doc_id'].unique())
           
             
             results_doc_level=pd.merge(results_sent_level2[['MCN','doc_id',"note_date","norm_term"]], results_sentence_level_temp, how="left", on="doc_id").drop_duplicates()
             a=len(results_doc_level)                 

            
             results_doc_level['sentence']= results_doc_level['sentence'].str.lstrip('~~')
             b=len(results_doc_level)
                
             if (a!=b):
                      print("*****************************************")
                      print("Error: something went wrong on adding sentences togethere")
                      print("*****************************************")
                 
             results_doc_level.to_excel(output_path+"tka_results_doc_level_"+version+".xlsx",index=False)     
             ############################################################
             postop_dx=med_tagger[med_tagger['section_name']=='SERGURY_POST_OPERATION_dx'][['MCN','doc_name', 'doc_id','note_date', 'covered_text', 'sentence','norm_term','status','term_status','section_name','sent_id']].drop_duplicates().sort_values(by="MCN")
             dx_sent_level, dx_doc_level= prepare_results(postop_dx)
             dx_doc_level.to_excel(output_path+"tka_results_dx_doc_level_"+version+".xlsx",index=False)  
             dx_sent_level.to_excel(output_path+"tka_results_dx_sent_level_"+version+".xlsx",index=False)   

             ############################################################
     
########################################
# Run the main block             
main()
     
     
     
     
     
     
     
