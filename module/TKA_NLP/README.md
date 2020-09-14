[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) 

# TKA - Total Knee Arthroplasty
  
## TKA NLP System
Process operative notes to extract five data elements: (1) category of surgery (total knee arthroplasty, unicompartmental knee arthroplasty, patellofemoral arthroplasty), (2) laterality of surgery, (3) constraint type, (4) presence of patellar resurfacing, and (5) implant model (catalog numbers)
@author Elham Sagheb, Sunyang Fu, Sunghwan Sohn, Walter Kremers, Ahmad P. Tafti, Taghi Ramazanian, Cody Wyles, Meagan Tibbo, David Lewallen, Daniel Berry, Hilal Maradit Kremers
 
## CONFIGURATION:
INPUT_DIR: full directory path of input folder
OUTPUT_DIR: full directory path of output folder
OUTPUT_SUMMARY_DIR: full directory path of output summary folder
RULES_DIR: full directory path of 'TKA' folder

## INPUT:
 Input folder: the input folder contains a list of surgical reports 
 Input file: document level .txt file. The naming convention of each report would be unique identifier + surgery date. P.S. one patient may have multiple surgeries. 
 Input file preprocessing: replace all '/n' to '. '

## RUN:

 1. Download MedTagger: https://github.com/OHNLP/TJA/tree/master/nlp_system 
 2. Move the .jar file to the TKA_NLP folder
 3. Edit the configuration .sh file
 3. command line:
 ```
 ./runMedTagger-fit-tka.sh
```
## OUTPUT:
 raw folder: concept level finding
 summary folder: document level finding

## REFERENCE: 
Use of Natural Language Processing Algorithms to Identify Common Data Elements in Operative Notes for Knee Arthroplasty. JOA-D-20-01740
