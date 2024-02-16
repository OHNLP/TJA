# PJI - Periprosthetic Joint Infection
  
## PJI NLP System
Process operative reports to automated detection of Periprosthetic Joint Infections and Data Elements Using Natural Language Processing.
@author Fu S, Wyles CC, Osmon DR, Carvour ML, Sagheb E, Ramazanian T, Kremers WK, Lewallen DG, Berry DJ, Sohn S, Kremers HM
 
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
Fu S, Wyles CC, Osmon DR, Carvour ML, Sagheb E, Ramazanian T, Kremers WK, Lewallen DG, Berry DJ, Sohn S, Kremers HM. Automated Detection of Periprosthetic Joint Infections and Data Elements Using Natural Language Processing. J Arthroplasty. 2021 Feb;36(2):688-692. doi: 10.1016/j.arth.2020.07.076. Epub 2020 Aug 5. PMID: 32854996; PMCID: PMC7855617.
