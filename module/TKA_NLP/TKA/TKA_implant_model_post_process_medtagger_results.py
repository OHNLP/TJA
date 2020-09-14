# -*- coding: utf-8 -*-

"""
Program Goals:
         This program is for extracting implant model for TKA operative notes
         We already have an output of medtagger,
         which contains the list of found terms for TKA implant type and their evidences 
         
         This program applies some rules to create final output for TKA implant model data element


"""
################  Edit Section #############################
# Devices data base can be downloaded from https://accessgudid.nlm.nih.gov/
devices_info_path="../implant_type/input/device.txt"
# name of the file and its directory which contains medtagger results
med_tagger_file="../implant_type/output/test/test.xlsx"
# ouptut directory that we can find output of this program there
output_path="../implant_type/output/test/"
# file which contains cohort list of the study
cohort_path="../implant_type/TKA Operative notes_selected_columns.xlsx"
# path which contains clinical notes 
note_path="../implant_type/input/test/"
#######################################################  
# Libraries
def open_libraries():
    global pd, os, datetime,np, re,fuzz, process
    import pandas as pd
    import os as os
    import datetime as datetime
    import numpy as np
    import re   as re
    from fuzzywuzzy import fuzz
    from fuzzywuzzy import process

    
#################
# Main program block
if __name__=='__main__':     
                
             # open libraries     
             open_libraries()
             
             ##################################
             # Read medtagger results from medtagger
             med_tagger=pd.read_excel(med_tagger_file, header=None)
             len(med_tagger)
                       
             med_tagger.columns=['doc_name','covered_text','norm_term','section_id','status','term_status',
                                 'experiencer','section_name','sentence','sent_id','begin','end']
             
             med_tagger['split']=med_tagger['doc_name'].str.split('_')
            
            
             for index, row in med_tagger.iterrows():
                 med_tagger.loc[index,'MCN']=row['split'][0]
                 med_tagger.loc[index,'doc_id']= row['split'][2].strip('.txt')
                 med_tagger.loc[index, 'note_date']=row['split'][1]
    
             # Exclude found numbers which are equal to patient number
             med_tagger['covered_text']=med_tagger['covered_text'].astype(str)
             med_tagger['covered_text2']=med_tagger['covered_text'].str.replace('\D','')
             med_tagger2=med_tagger[med_tagger['covered_text2']!=med_tagger['MCN'].astype(str)]
             
             # fill sent_id null with Null:1
             med_tagger2.loc[ med_tagger2['sent_id'].isnull(),'sent_id']='Null:1'
             a=med_tagger[med_tagger['sent_id']=='Null:1']
             
             # exclude those which were found after 10th sentence in a section 
             med_tagger2['sent_id2']=med_tagger2['sent_id'].str.replace('.*:','')
             med_tagger2=med_tagger2[~med_tagger2['sent_id2'].isnull()]
             med_tagger2['sent_id2']=med_tagger2['sent_id2'].astype(int)
             med_tagger2=med_tagger2[med_tagger2['sent_id2']<=13]
             
             # exclude those which are equal to the convered sentence since they are just section numbers
             med_tagger2=med_tagger2[med_tagger2['sentence'].str.replace(':','')!=med_tagger2['covered_text']]
             
             # exclude those which their covered_text contains ":"
             med_tagger2=med_tagger2[~med_tagger2['covered_text'].str.contains(':')]
             
             
             # 
             med_tagger3=med_tagger.copy()
             med_tagger=med_tagger2
    
    
             print(med_tagger['MCN'].nunique())
             print(med_tagger['doc_name'].nunique())
 
             file_list=os.listdir(note_path)
             file_list_pd=pd.DataFrame(file_list)
             file_list_pd.columns=['doc_name']
             missing_doc=file_list_pd[~file_list_pd['doc_name'].isin(med_tagger['doc_name'].tolist())]
             print(len(missing_doc))


             med_tagger['covered_text']=med_tagger['covered_text'].astype(str)
             med_tagger['model_number']=med_tagger['covered_text'].str.strip(';').str.strip(',').str.strip('#').str.strip()
                       
             med_tagger2=med_tagger.copy()      
             print(len(med_tagger2))
             print(len(med_tagger2[['doc_name']].drop_duplicates()))
             
             
             model_numbers=med_tagger2[med_tagger2['norm_term']=='Model_Number']
             model_numbers['model_number']=model_numbers['model_number'].str.rstrip(',')
             model_numbers['model_number3']=model_numbers['model_number'].str.lstrip('0').str.replace('-','').str.replace('_','')
             model_numbers['model_number4']=model_numbers['model_number'].str.lstrip('0').str.replace('-','').str.replace('_','').str.strip()
             model_numbers=model_numbers[~(model_numbers['model_number4'].str.contains(r'^(2|3)\d\d\d\d\d$'))]
             ###########################
             # save the list of all notes inot a dataframe
             doc_list=os.listdir(note_path)
             all_files=pd.DataFrame()
             for file in doc_list:
                 with open(note_path+file, 'r') as content_file:
                        content = content_file.read()
                        
                 
                 mcn=file.split('_')[0]
                 note_date=file.split('_')[1]
                 
                 temp=pd.DataFrame({'MCN':[mcn],'doc_name':[file],'note_date':[note_date],'note':[content]})
                  
                 all_files=all_files.append(temp)
                 
             all_files=all_files.reset_index(drop=True)  
             all_files.to_excel(output_path+"all_files.xlsx",index=False)
            
            
            ########
            # read the original cohort of TKA to merge with all notes 
             cohort=pd.read_excel(cohort_path)
             cohort['note_date']=pd.to_datetime(cohort['note_date'])
             cohort['MCN']=cohort['MCN'].astype(int)
             all_files['note_date']=pd.to_datetime(all_files['note_date'])
             all_files['MCN']=all_files['MCN'].astype(int)
             cohort['MCN']=cohort['MCN'].astype(int)
            
            
             cohort_notes=pd.merge(all_files,cohort, on=['MCN','note_date'], how='left')
             print(len(cohort_notes))
            
            
             cohort=cohort_notes
             cohort.columns=cohort.columns.astype(str)
             cohort_notes.to_excel(output_path+"cohort_notes.xlsx",index=False)
           
            #########
 
             def find_missings(column_):

                 temp=cohort[['note_date','MCN',column_]].drop_duplicates()
                 print(len(temp))
                 # normalize implant model number
                 temp['temp']=temp[column_].str.lstrip('0').str.replace('-','').str.replace('_','')
                
                 all_files['note_date']=pd.to_datetime(all_files['note_date'])
                 all_files['MCN']=all_files['MCN'].astype(int)
                 temp['note_date']=pd.to_datetime(temp['note_date'])
                 temp['MCN']=temp['MCN'].astype(int)
                 cohort2=pd.merge(all_files,temp,how='left',on=['note_date','MCN'])
                 print(len(cohort2))
                 cohort3=cohort2[~cohort2[column_].isnull()].drop_duplicates()
                 print(len(cohort3))
                
                
          
                ############ 
                
                
                # link of cohort and nlp results
                 model_numbers['note_date']=pd.to_datetime(model_numbers['note_date'])
                 model_numbers['MCN']=model_numbers['MCN'].astype(int)
                 model_numbers['model_number4']=model_numbers['model_number4'].str.strip()
                 nlp_missing2=pd.merge(cohort3, model_numbers, left_on=['note_date','MCN','temp'], right_on=['note_date','MCN','model_number4'], how='left')
                 missing2=nlp_missing2[nlp_missing2['model_number4'].isnull()]   
                 mapped=nlp_missing2[~nlp_missing2['model_number4'].isnull()]   
                 mapped['category']=column_
                 missing2.to_excel(output_path+'missing2'+column_+'.xlsx', index=False)
                
                 a=pd.DataFrame()
                 b=pd.DataFrame()
                 for index , row in missing2.iterrows():
                    if row['note'].find(row[column_])>=0:
                        print(row['doc_name_x'])
                        a=a.append(model_numbers[model_numbers['doc_name']==row['doc_name_x']])
                        temp=med_tagger[med_tagger['doc_name']==row['doc_name_x']]
                        temp['missing_model']=row[column_]
                        temp['category']=column_
                        b=b.append(temp)
                        print(row[column_])
                        
                 return(b,mapped)
                           
                 ########
                 missing=pd.DataFrame()
                 mapped=pd.DataFrame()
                 mapped_models=pd.DataFrame()
                 
                 
                 for col in ['10','20','30','40','IMPLANT_NUMBER1','IMPLANT_NUMBER1.1']:
                      missing2,mapped2=find_missings(col)
                      mapped=mapped.append(mapped2)
                      missing=missing.append(missing2)
                      mapped_models_temp=mapped[[col]].drop_duplicates()
                      mapped_models_temp.columns=['model_number5']
                      mapped_models=mapped_models.append(mapped_models_temp)
                      
                     
                 
                 print(len(mapped))
                 print(len(model_numbers))
                 missing.to_excel(output_path+'missing_records'+'.xlsx', index=False)
                 mapped.to_excel(output_path+'mappded_records'+'.xlsx', index=False)
                 mapped_models['model_number4']=mapped_models['model_number5'].str.lstrip('0').str.replace('-','').str.replace('_','').str.strip()
                 a=model_numbers[~model_numbers['model_number4'].isin(mapped_models['model_number4'].tolist())]
                 a.to_excel(output_path+"missied_by_ann.xlsx",index=False)
               
             
              
             
             
            
             #########################
             # Load device information
             devices_info=pd.read_csv(devices_info_path,delimiter='|',low_memory=False)
             print(len(devices_info))
             
             devices_info['model_number']=devices_info['catalogNumber']
             print(len(devices_info['model_number'].unique()))
             
             print(len(devices_info['versionModelNumber'].unique()))
             
             print(len(devices_info['PrimaryDI'].unique()))
            
             print(len(devices_info[['model_number','versionModelNumber']].drop_duplicates()))
             
                       
#            ############################ 
             # get rid of dashes and leading 0 from all model_numbers
             devices_info['model_number1']=devices_info['model_number']
             devices_info['model_number']=devices_info['model_number'].str.lstrip('0').str.replace('-','')
             devices_info['model_number3']=devices_info['model_number'].str.lstrip('0').str.replace('-','').str.replace('_','')
             devices_info=devices_info.fillna({'model_number':'aa'})
             devices_info['model_number4']=devices_info['versionModelNumber'].str.lstrip('0').str.replace('-','').str.replace('_','')

             ######################################
             # merge med tagger results with device information
             med_number2=pd.merge(model_numbers, devices_info, how='left',on='model_number3')
             print(len(med_number2))
              # Find records with not matched devices
             missing_model_number=med_number2[med_number2['PrimaryDI'].isnull()]
             print(len(missing_model_number))
             print(len(model_numbers))
             
             # keep thoes with mapped device information
             notes_with_device_info=med_number2[~med_number2['PrimaryDI'].isnull()]
             print(len(notes_with_device_info))
             
             # merge records without mapped devices with devices data file on versionModelNumber field
             m2=model_numbers[model_numbers['model_number3'].isin(missing_model_number['model_number3'].tolist())]
             devices_info['model_number4']=devices_info['versionModelNumber'].str.lstrip('0').str.replace('-','').str.replace('_','')
             m3=pd.merge(m2, devices_info, how='left',on='model_number4')
             print(len(m3))
             missing_m3=m3[m3['PrimaryDI'].isnull()]
             print(len(missing_m3))
             # add to gether records with mapped devices 
             notes_with_device_info=notes_with_device_info.append(m3[~m3['PrimaryDI'].isnull()])
             print(len(notes_with_device_info))
             print(len(notes_with_device_info['doc_name'].drop_duplicates()))
             # find the duplicates, multiple devices have assined to same model_numbers
             temp=notes_with_device_info[['doc_name','model_number','PrimaryDI']].drop_duplicates()
             multiples1=temp.groupby(['doc_name','model_number'])['PrimaryDI'].count().reset_index()
             multiples=multiples1[multiples1['PrimaryDI']>=2]
             multiple_in_notes_with_device_info= notes_with_device_info[(notes_with_device_info['doc_name'].isin(multiples['doc_name'].tolist())) &
                                                                        (notes_with_device_info['model_number'].isin(multiples['model_number']))]
             
             print(" Counts of duplicates (count of implants which mapped to more than one device id):")
             print(len(multiple_in_notes_with_device_info))
             # for those with multiple assinged primaryID we can pick the one which published closest to the note_date
             notes_with_device_info['note_date']=pd.to_datetime(notes_with_device_info['note_date'])
             notes_with_device_info['publicVersionDate']=pd.to_datetime(notes_with_device_info['publicVersionDate'])
             notes_with_device_info['note_date_publish_date']=(notes_with_device_info['note_date']-notes_with_device_info['publicVersionDate'])
             notes_with_device_info=notes_with_device_info.fillna({'note_date_publish_date':0})
             notes_with_device_info['note_date_publish_date2']=notes_with_device_info['note_date_publish_date'].dt.days.astype(int)     
             notes_with_device_info=notes_with_device_info.drop("split",axis=1).drop_duplicates()
             notes_with_device_info['note_date_publish_date2']=abs(notes_with_device_info['note_date_publish_date2'])
             notes_with_device_info2=notes_with_device_info.loc[notes_with_device_info.groupby(["doc_name","model_number3"])['note_date_publish_date2'].idxmin()]
            
             notes_with_device_info2=notes_with_device_info2.drop_duplicates()
            
             print(len(notes_with_device_info2))
             
             print(len(notes_with_device_info2['doc_name'].drop_duplicates()))

             
             ###########################################                       
             # Save the results
             notes_with_device_info.to_excel(output_path+"notes_and_mapped_devices.xlsx",index='False')
             print(len(notes_with_device_info))
             #5294
     
     
     