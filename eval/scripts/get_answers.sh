export PYTHONPATH=${PWD}:${PYTHONPATH}
num_gpus=1
lang=${1}
model_path=${2}
model_id="$(echo "${model_path}" | rev | cut -d '/' -f 1 | rev)"

python eval/vicuna_eval/get_model_answers.py \
 --model-id "${model_id}" \
 --model-path "${model_path}" \
 --question-file "eval/vicuna_eval/questions/questions_${lang}.jsonl" \
 --answer-file "eval/vicuna_eval/answers/${lang}/${model_id}.jsonl" \
 --num-gpus ${num_gpus}