#/bin/bash

#change into full directory
INPUT_DIR="/TKA_Deploy/TKA_NLP/input/"
OUTPUT_DIR="/TKA_Deploy/TKA_NLP/output/raw/"


RULES_DIR_1="/TKA_Deploy/TKA_NLP/TKA/TKA_category_of_surgery"
RULES_DIR_2="/TKA_Deploy/TKA_NLP/TKA/TKA_constraint_type"
RULES_DIR_3="/TKA_Deploy/TKA_NLP/TKA/TKA_implant_model"
RULES_DIR_4="/TKA_Deploy/TKA_NLP/TKA/TKA_laterality_of_surgery"
RULES_DIR_5="/TKA_Deploy/TKA_NLP/TKA/TKA_presence_of_patellar_resurfacing"

#No need to change
OUTPUT_DIR_1="${OUTPUT_DIR}category_of_surgery"
OUTPUT_DIR_2="${OUTPUT_DIR}constraint_type"
OUTPUT_DIR_3="${OUTPUT_DIR}implant_model"
OUTPUT_DIR_4="${OUTPUT_DIR}laterality_of_surgery"
OUTPUT_DIR_5="${OUTPUT_DIR}presence_of_patellar_resurfacing"
OUTPUT_SUMMARY_DIR="/output/summary"

java -Xms512M -Xmx2000M -jar MedTagger-fit-1.0.2-SNAPSHOT.jar $INPUT_DIR_1 $OUTPUT_DIR_1 $RULES_DIR_1
java -Xms512M -Xmx2000M -jar MedTagger-fit-1.0.2-SNAPSHOT.jar $INPUT_DIR_2 $OUTPUT_DIR_2 $RULES_DIR_2
java -Xms512M -Xmx2000M -jar MedTagger-fit-1.0.2-SNAPSHOT.jar $INPUT_DIR_3 $OUTPUT_DIR_3 $RULES_DIR_3
java -Xms512M -Xmx2000M -jar MedTagger-fit-1.0.2-SNAPSHOT.jar $INPUT_DIR_4 $OUTPUT_DIR_4 $RULES_DIR_4
java -Xms512M -Xmx2000M -jar MedTagger-fit-1.0.2-SNAPSHOT.jar $INPUT_DIR_5 $OUTPUT_DIR_5 $RULES_DIR_5


#Use "1" for Window System; Unix/Linux/Mac for "0"
python TKA/TKA_category_of_surgery-post-process-medtagger-results.py $OUTPUT_DIR $OUTPUT_SUMMARY_DIR "0"
python TKA_constraint_type-post_process-medtagger_results.py         $OUTPUT_DIR $OUTPUT_SUMMARY_DIR "0"
python TKA_implant_model_post_process_medtagger_results.py           $OUTPUT_DIR $OUTPUT_SUMMARY_DIR "0"
python TKA_laterality_of_surgery-process-medtagger_results.py        $OUTPUT_DIR $OUTPUT_SUMMARY_DIR "0"
python TKA_presence_of_patella_resurfacing-_post_process-medtagger_results.py $OUTPUT_DIR $OUTPUT_SUMMARY_DIR "0"