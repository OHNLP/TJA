[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) 

# PPFX - Periprosthetic Femur Fractures module
  
## PPFX NLP System
Process operative reports to identify periprosthetic femur fractures (PPFFx) followed by more complex Vancouver classification.
@author Tibbo ME, Wyles CC, Fu S, Sohn S, Lewallen DG, Berry DJ, Maradit Kremers H.

## CONFIGURATION:
INPUT_DIR: full directory path of input folder
OUTPUT_DIR: full directory path of output folder
OUTPUT_SUMMARY_DIR: full directory path of output summary folder
RULES_DIR: full directory path of 'TJA' folder

## INPUT:
 Input folder: the input folder contains a list of surgical reports 
 Input file: document level .txt file. The naming convention of each report would be unique identifier + surgery date. P.S. one patient may have multiple surgeries. 
 Input file preprocessing: replace all '/n' to '. '

## RUN:
 command line:
 ```
 ./runMedTagger-fit-tja.sh
```
## OUTPUT:
 raw folder: concept level finding
 summary folder: document level finding

## REFERENCE: 
Tibbo ME, Wyles CC, Fu S, Sohn S, Lewallen DG, Berry DJ, Maradit Kremers H. Use of Natural Language Processing Tools to Identify and Classify Periprosthetic Femur Fractures. J Arthroplasty. 2019 Oct;34(10):2216-2219. doi: 10.1016/j.arth.2019.07.025. Epub 2019 Jul 24. PMID: 31416741; PMCID: PMC6760992.
