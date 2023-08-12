export PYTHONPATH=${PWD}:${PYTHONPATH}
lang=${1}
model_path=${2}
model_id=${3}

python eval/vicuna_eval/get_model_answers.py \
 --model-id "${model_id}" \
 --model-path "${model_path}" \
 --question-file "eval/vicuna_eval/questions/questions_${lang}.jsonl" \
 --answer-file "eval/vicuna_eval/answers/${lang}/${model_id}.jsonl" \
 --num-gpus 1