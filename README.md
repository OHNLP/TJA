# TJA
NLP Algorithms for Total Joint Arthroplasty

## THA NLP System
Process operative reports to classify a patient's status of approach, fixation and bearing surface
@author Sunyang Fu, Sunghwan Sohn, Hilal Maradit Kremers, Walter Kremers, Ahmad Pahlavan Tafti, Elham Sagheb Hossein Pour, Cody Wyles, Meagan Tibbo, David Lewallen, Daniel Berry

## TKA NLP System
Process operative notes to extract five data elements: (1) category of surgery (total knee arthroplasty, unicompartmental knee arthroplasty, patellofemoral arthroplasty), (2) laterality of surgery, (3) constraint type, (4) presence of patellar resurfacing, and (5) implant model (catalog numbers)
@author Elham Sagheb, Sunyang Fu, Sunghwan Sohn, Walter Kremers, Ahmad P. Tafti, Taghi Ramazanian, Cody Wyles, Meagan Tibbo, David Lewallen, Daniel Berry, Hilal Maradit Kremers

# MedTagger
MedTagger contains a suite of programs that the Mayo Clinic NLP program has developed in 2013.
It includes three major components: MedTagger for indexing based on dictionaries, MedTaggerIE for
information extraction based on patterns, and MedTaggerML for machine learning-based named entity recognition.
#### MedTagger git repo: https://github.com/OHNLP/MedTagger
#### Video demo: https://vimeo.com/392331446

1. Download the latest release from https://github.com/OHNLP/MedTagger/releases
2. Extract the zip file
3. Modify the `INPUTDIR`, `OUTPUTDIR`, and `RULEDIR` variables in `run_medtagger_win.bat` or `run_medtagger_unix_mac.sh`, as appropriate
    - `INPUT_DIR`: full directory path of input folder 
    - `OUTPUT_DIR`: full directory path of output folder
    - `RULES_DIR`: full directory path of 'Rule' folder
    
    Example for Mac:
    ```
    INPUTDIR="$YOUR_INPUT_DIRECTORY"
    OUTPUTDIR="$YOUR_OUTPUT_DIRECTORY"
    RULEDIR="$YOUR_MEDTAGGER_HOME/medtaggerieresources/covid19"
    ```
    
    Example for Windows:
    ```
    INPUTDIR="C:\$YOUR_INPUT_DIRECTORY\input"
    OUTPUTDIR="C:\$YOUR_OUTPUT_DIRECTORY\output"
    RULEDIR="C:\YOUR_MEDTAGGER_HOME\medtaggerieresources\covid19"
    ```
    
4. Run the batch file

    Mac/linux: 
    ```
    run_medtagger_unix_mac.sh
    ```
    
    Windows: 
    
    ```
    run_medtagger_win.bat
    ```
