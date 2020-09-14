# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 08:32:37 2018

@author: Elham sagheb
 
Program Goals:
         THis progrma is to exteract patella resourfacing data element
         We have already an output from medtagger,
         which contains the list of found terms for patella resourfacing their evidence 
         
         This program applies some rules to create final output for the TKA patella resourfacing data element

"""
################  Edit Section #############################
# put med_tagger output results file and its path in the below line
med_tagger_file="../output/patella/test/patella_test.txt"

# put the name of directory that you want to see the output files 
output_path="../output/patella/test/"

#######################################################  


###################################
# This method open liberaries
def open_libraries():
    global pd, os, datetime,np, re
    import pandas as pd
    import os as os
    import datetime as datetime
    import numpy as np
    import re   as re

##########################################
          


#####################################
def process_surgery_date(table1):
          table2=table1[table1['norm_term']=='Surgery_Date']  
          table2['split']=table2['sentence'].str.split(':')  
          for index, row in table2.iterrows():
               if row['sentence'].find("Date ")>=0:
                    table2.at[index,'date_raw']=row['split'][1].strip()[0:12]
               else:
                    table2.at[index,'date_raw']=row['split'][0].replace('Surg','').strip()[0:8]
                    
          table2['surge_date']=pd.to_datetime(table2['date_raw'])   
          return(table2[['doc_id','surge_date']].drop_duplicates())
#####################################
def prepare_doc_and_sentence_level_results(table):
                      
             table_sentence_level=table[['MCN','doc_name', 'note_date','surge_date','covered_text', 'norm_term', 'section_id', 
                                           'status', 'term_status','experiencer', 'section_name',  'sentence', 'sent_id',   
                                           'doc_id', 'version', 'dep', 'dep2', 'note_date']]
             ####################
             table.loc[table['status']!='Negated','final_status']='YES'
             table.loc[table['status']=='Negated','final_status']='NO'

            
             #####################################
             #concatinate the found sentences and add the 
             table['evidence']= table['doc_name']+"::"+table['status']+"::"+table['section_id'].astype(str)+"::"+table["section_name"]+"::"+table["sentence"]+"~~"
             table_sentence=table[['doc_id','final_status','evidence']].groupby(['doc_id','final_status'])['evidence'].sum().reset_index()
             doc_list=table[['MCN','doc_id','note_date','surge_date']].drop_duplicates()
             
             table_doc_level=pd.merge(doc_list , table_sentence, how="left", on="doc_id")
             
             ##################################
             return(table_doc_level, table_sentence_level)                
  
           
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
             #
            
           
            
             
             med_tagger.columns=['doc_name','covered_text','norm_term','section_id','status','term_status',
                                 'experiencer','section_name','sentence','sent_id','begin','end']
            
        
             
             med_tagger['split']= med_tagger['doc_name'].str.split('_')
             med_tagger[['MCN','doc_id','version','dep','dep2','note_date']]= pd.DataFrame(med_tagger.split.values.tolist(), index=med_tagger.index)
             
             med_tagger['sent_id']=med_tagger['sent_id'].str.replace(".*:","")
             print(med_tagger['MCN'].nunique())
             

             
             # seperate surgery_dates
             surgery_dates=process_surgery_date(med_tagger)

             # ignore "surgery_dates" norm_term
             med_tagger=med_tagger[med_tagger['norm_term']!='Surgery_Date']
             len(med_tagger)
            
             
            
             
             # add surgery date to med_tagger
             med_tagger2=pd.merge(med_tagger,surgery_dates,how="left",on="doc_id")
             
             # just use the cocepts within specific sections
             med_tagger3=med_tagger2[      (med_tagger2['covered_text'].str.contains('-'))  
                                     |     (med_tagger2['section_name'].isin(['Implant Name','GRAFT/IMPLANT INFORMATION','Name','PREOP DIAGNOSIS',' Lot/Serial #']))
                                     |     (med_tagger2['norm_term']=='Patella_terms')]
    
             med_tagger3=med_tagger2[(med_tagger2['norm_term']=='Patella_terms')]
    
             med_tagger4=med_tagger3[(med_tagger3['sentence'].str.lower().str.contains('no\.')) | (med_tagger3['status']!='Negated')]
             
             # keep just mentions on procedure section
             results_doc_level, results_sentence_level=prepare_doc_and_sentence_level_results(med_tagger4)
             
             # save the outputs
             results_doc_level.to_excel(output_path+"patella_doc_level.xlsx",index=False)
             results_sentence_level.to_excel(output_path+"patella_sentence_level.xlsx",index=False)
             surgery_dates.to_excel(output_path+"patella_surgery_dates.xlsx",index=False)
             
             
  












