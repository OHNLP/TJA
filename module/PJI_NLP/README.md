# PJI - Periprosthetic Joint Infection
  
## PJI NLP System
Process consultation notes, operative notes, pathology reports, and microbiology reports to automated detection of Periprosthetic Joint Infections and Data Elements Using Natural Language Processing.
@author Fu S, Wyles CC, Osmon DR, Carvour ML, Sagheb E, Ramazanian T, Kremers WK, Lewallen DG, Berry DJ, Sohn S, Maradit Kremers H.
 
## CONFIGURATION and Run:
1- Extracting information from clinical notes:
You need to extract "Acute Inflammation" from pathology notes, "Sinus Tract" from clinical visit notes, and "Purulent Material" from operative notes.

1-1. Download the latest medtaagger release from https://github.com/OHNLP/TJA/tree/master/nlp_system 
1-2. Move the .jar file to either PPFX_NLP folder
1-3. Modify the `INPUTDIR`, `OUTPUTDIR`, and `RULEDIR` variables in `runMedTagger-fit-PJI.sh`.
    - `INPUT_DIR`: full directory path of input folder 
    - `OUTPUT_DIR`: full directory path of output folder
    - `RULES_DIR`: full directory path of 'Rule' folder
    
    Example:
    ```
    INPUTDIR="$YOUR_INPUT_DIRECTORY"
    OUTPUTDIR="$YOUR_OUTPUT_DIRECTORY"
    RULEDIR="$YOUR_MEDTAGGER_HOME/medtaggerieresources/covid19"
    ```
    
1-4. Run the batch file

    ```
    run_medtagger_unix_mac.sh
    ```
2- Combine the extracted information from step 1 with microbiology lab results based on the algorithm in the below figure to obtain final PJI status.
![Process for extracting and classifying PJI status](https://raw.githubusercontent.com/OHNLP/TJA/master/module/PJI_NLP/nihms-1623200-f0001.jpg)




## REFERENCE: 
Fu S, Wyles CC, Osmon DR, Carvour ML, Sagheb E, Ramazanian T, Kremers WK, Lewallen DG, Berry DJ, Sohn S, Maradit Kremers H. Automated Detection of Periprosthetic Joint Infections and Data Elements Using Natural Language Processing. J Arthroplasty. 2021 Feb;36(2):688-692. doi: 10.1016/j.arth.2020.07.076. Epub 2020 Aug 5. PMID: 32854996; PMCID: PMC7855617.
