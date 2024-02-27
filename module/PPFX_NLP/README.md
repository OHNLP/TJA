[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) 

# PPFX - Periprosthetic Femur Fractures module
  
## PPFX NLP System
Process operative reports to identify periprosthetic femur fractures (PPFFx) followed by more complex Vancouver classification.
@author Tibbo ME, Wyles CC, Fu S, Sohn S, Lewallen DG, Berry DJ, Maradit Kremers H.

## Configuration and Run:

1. Download the latest medtaagger release from https://github.com/OHNLP/TJA/tree/master/nlp_system 
2. Move the .jar file to either PPFX_NLP folder
3. Modify the `INPUTDIR`, `OUTPUTDIR`, and `RULEDIR` variables in `runMedTagger-fit-tja.sh` or `runMedTagger-fit-tka.sh`, as appropriate
    - `INPUT_DIR`: full directory path of input folder 
    - `OUTPUT_DIR`: full directory path of output folder
    - `RULES_DIR`: full directory path of 'Rule' folder
    
    Example:
    ```
    INPUTDIR="$YOUR_INPUT_DIRECTORY"
    OUTPUTDIR="$YOUR_OUTPUT_DIRECTORY"
    RULEDIR="$YOUR_MEDTAGGER_HOME/medtaggerieresources/covid19"
    ```
    
4. Run the batch file

    ```
    run_medtagger_unix_mac.sh
    ```
## REFERENCE:
https://pubmed.ncbi.nlm.nih.gov/31416741/

Tibbo ME, Wyles CC, Fu S, Sohn S, Lewallen DG, Berry DJ, Maradit Kremers H. Use of Natural Language Processing Tools to Identify and Classify Periprosthetic Femur Fractures. J Arthroplasty. 2019 Oct;34(10):2216-2219. doi: 10.1016/j.arth.2019.07.025. Epub 2019 Jul 24. PMID: 31416741; PMCID: PMC6760992.
