INPUT_FILES="$(pwd)/resources/datasets/longsumm/*"
INPUT_DIR="$(pwd)/resources/datasets/longsumm/"
OUTPUT_DIR="$(pwd)/predictions/"

#python scripts/generate.py < resources/datasets/asset/asset.test.complex > asset_model.pred


for file in ${INPUT_FILES}; do
  filename=$(basename -- "$file")
  echo "${filename}"
  suffix="${filename##*[0-9]}"
  number="${filename%"$suffix"}"
  number="${number##*[!-0-9]}"
  echo "${number}"

  python scripts/generate.py < "${INPUT_DIR}${filename}" > "${OUTPUT_DIR}/longsumm.test.pred.${number}"
done
  
