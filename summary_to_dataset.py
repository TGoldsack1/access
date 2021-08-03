'''
Converts n outputted pointer-generator summaries into an 
n ACCESS tests file consistens of a sentence on every line.
Authors: Tomas + Zhihao
'''


import os, ast
from nltk.tokenize import sent_tokenize

summary_dir = "./summaries"
output_dir = "./resources/datasets/longsumm"

# Select which summary file to create test dataset from
#json_output_file = summary_dir + "/my_longsumm_test_AIC_my_pretrained_allenai_output.json"
json_output_file = summary_dir + "/my_longsumm_test_AIC_news_pretrained_allenai_output.json"


# handle output of the allen ai PG model
if "allenai" in json_output_file: 
  file_content = open(json_output_file, "r")
  file_lines = file_content.readlines()
  file_content.close()

  for i, line in enumerate(file_lines):
    summary = ast.literal_eval(line)["prediction"]

    output_file = open(output_dir + "/longsumm.test.complex." + str(i), "w")
    
    for sentence in sent_tokenize(summary):
      output_file.write(sentence + "\n")

    output_file.close()
