#/bin/bash

#change into full directory
INPUT_DIR="/TJA_Deploy/TJA_NLP/input/"
OUTPUT_DIR="/TJA_Deploy/TJA_NLP/output/raw/"
RULES_DIR_FX="/TJA_Deploy/TJA_NLP/TJA/THA_fixation"
RULES_DIR_BE="/TJA_Deploy/TJA_NLP/TJA/THA_bearing"
RULES_DIR_AP="/TJA_Deploy/TJA_NLP/TJA/THA_approach"

#No need to change
OUTPUT_DIR_AP="${OUTPUT_DIR}approach"
OUTPUT_DIR_BE="${OUTPUT_DIR}bearing"
OUTPUT_DIR_FX="${OUTPUT_DIR}fixation"
OUTPUT_SUMMARY_DIR="/output/summary"

java -Xms512M -Xmx2000M -jar MedTagger-fit-1.0.2-SNAPSHOT.jar $INPUT_DIR $OUTPUT_DIR_AP $RULES_DIR_AP
java -Xms512M -Xmx2000M -jar MedTagger-fit-1.0.2-SNAPSHOT.jar $INPUT_DIR $OUTPUT_DIR_FX $RULES_DIR_FX
java -Xms512M -Xmx2000M -jar MedTagger-fit-1.0.2-SNAPSHOT.jar $INPUT_DIR $OUTPUT_DIR_BE $RULES_DIR_BE

#Use "1" for Window System; Unix/Linux/Mac for "0"
python TJA/model/output_tja.py $OUTPUT_DIR $OUTPUT_SUMMARY_DIR "0"