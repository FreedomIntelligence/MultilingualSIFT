export PYTHONPATH=${PWD}:${PYTHONPATH}
lang=${1}
model_path=${2}
model_id=${3}

python -m eval.mmlu.run_eval \
 --ntrain 0 \
 --data_dir "data/eval/mmlu_${lang}/" \
 --save_dir "results/mmlu_${lang}/${model_id}-5shot/" \
 --model_name_or_path "${model_path}" \
 --tokenizer_name_or_path "${model_path}" \
 --eval_batch_size 2 \
 --load_in_8bit --use_chat_format