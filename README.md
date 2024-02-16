# TJA
NLP Algorithms for Total Joint Arthroplasty

## THA NLP System
Process operative reports to classify a patient's status of approach, fixation and bearing surface
@author Sunyang Fu, Sunghwan Sohn, Hilal Maradit Kremers, Walter Kremers, Ahmad Pahlavan Tafti, Elham Sagheb Hossein Pour, Cody Wyles, Meagan Tibbo, David Lewallen, Daniel Berry
#### THA module: https://github.com/OHNLP/TJA/tree/master/module/THA_NLP

## TKA NLP System
Process operative notes to extract five data elements: (1) category of surgery (total knee arthroplasty, unicompartmental knee arthroplasty, patellofemoral arthroplasty), (2) laterality of surgery, (3) constraint type, (4) presence of patellar resurfacing, and (5) implant model (catalog numbers)
@author Elham Sagheb, Sunyang Fu, Sunghwan Sohn, Walter Kremers, Ahmad P. Tafti, Taghi Ramazanian, Cody Wyles, Meagan Tibbo, David Lewallen, Daniel Berry, Hilal Maradit Kremers
#### TKA module: https://github.com/OHNLP/TJA/tree/master/module/TKA_NLP

## PJI NLP System
Process operative reports to automated detection of Periprosthetic Joint Infections and Data Elements Using Natural Language Processing. 
@author Fu S, Wyles CC, Osmon DR, Carvour ML, Sagheb E, Ramazanian T, Kremers WK, Lewallen DG, Berry DJ, Sohn S, Kremers HM
#### PJI module: https://github.com/OHNLP/TJA/tree/master/module/PJI_NLP

## PPFX NLP System
Process operative reports to identify periprosthetic femur fractures (PPFFx) followed by more complex Vancouver classification.                 
@author Tibbo ME, Wyles CC, Fu S, Sohn S, Lewallen DG, Berry DJ, Maradit Kremers H.
#### PPFX module: https://github.com/OHNLP/TJA/tree/master/module/PPFX_NLP

# MedTagger
MedTagger contains a suite of programs that the Mayo Clinic NLP program has developed in 2013.
It includes three major components: MedTagger for indexing based on dictionaries, MedTaggerIE for
information extraction based on patterns, and MedTaggerML for machine learning-based named entity recognition.
#### MedTagger git repo: https://github.com/OHNLP/MedTagger
#### Video demo: https://vimeo.com/392331446
#### Original release: https://github.com/OHNLP/MedTagger/releases

1. Download the latest release from https://github.com/OHNLP/TJA/tree/master/nlp_system 
2. Move the .jar file to either THA_NLP or TKA_NLP
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
    
# Publications
THA NLP System:  https://pubmed.ncbi.nlm.nih.gov/31567670/

TKA NLP System:  https://pubmed.ncbi.nlm.nih.gov/33051119/

PJI NLP System:  https://pubmed.ncbi.nlm.nih.gov/32854996/

PPFX NLP System: https://pubmed.ncbi.nlm.nih.gov/31416741/

