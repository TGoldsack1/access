'''
Converts n outputted ACCESS simplified sentences back into a
summary paragraph and adds them to the original json files (outputted
from the pointer generator).
Authors: Tomas + Zhihao
'''


import os, ast, json

summary_dir = "./summaries/"

# Select which summary file to create test dataset from
#predictions_dir = "./predictions/allenai_my_pretrained"
#json_output_file = summary_dir + "/my_longsumm_test_AIC_my_pretrained_allenai_output.json"
predictions_dir = "./predictions/allenai_my_pretrained"
json_output_file = "my_longsumm_test_AIC_my_pretrained_allenai_output.json"

# Set input/output file names
json_output_filepath = summary_dir + json_output_file
simplified_output_filepath = summary_dir + "simplified_" + json_output_file

if "allenai" in json_output_filepath: 
  file_content = open(json_output_filepath, "r")
  file_lines = file_content.readlines()
  file_content.close()

  output_file = open(simplified_output_filepath, "w")

  for i, line in enumerate(file_lines):
    output_dict = ast.literal_eval(line)
    
    # Get simplified ACCESS predictions
    simplified_pred_file = open(predictions_dir + "/longsumm.test.pred." + str(i), "r")
    simplified_pred_lines = [x.strip() for x in simplified_pred_file.readlines()]
    simplified_pred_file.close()

    # Concatenate simplified sententeces to form a simplified summary 
    output_dict["simplified_prediction"] = " ".join(simplified_pred_lines)

    # Write a copy of the summary file including the simplified output
    output_file.write(json.dumps(output_dict) + "\n")

  output_file.close()