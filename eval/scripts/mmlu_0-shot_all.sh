# Hyper-parameters
model_path=${1}
model_name="$(echo "${model_path}" | rev | cut -d '/' -f 1 | rev)"  # bloom-560m

echo "${model_name[0]}"

# MMLU (5-shot)
python -m eval.mmlu.run_eval \
    --ntrain 0 \
    --data_dir data/eval/mmlu/ \
    --save_dir results/mmlu-0shot/"${model_name}"-0shot/ \
    --model_name_or_path "${model_path}" \
    --tokenizer_name_or_path "${model_path}" \
    --eval_batch_size 2 \
    --load_in_8bit --use_chat_format

lang=Chinese
# MMLU (5-shot)
python -m eval.mmlu.run_eval \
    --ntrain 0 \
    --data_dir data/eval/mmlu_${lang}/ \
    --save_dir results/mmlu_${lang}-0shot/"${model_name}"-0shot/ \
    --model_name_or_path "${model_path}" \
    --tokenizer_name_or_path "${model_path}" \
    --eval_batch_size 2 \
    --load_in_8bit --use_chat_format

lang=French
# MMLU (5-shot)
python -m eval.mmlu.run_eval \
    --ntrain 0 \
    --data_dir data/eval/mmlu_${lang}/ \
    --save_dir results/mmlu_${lang}-0shot/"${model_name}"-0shot/ \
    --model_name_or_path "${model_path}" \
    --tokenizer_name_or_path "${model_path}" \
    --eval_batch_size 2 \
    --load_in_8bit --use_chat_format


lang=Spanish
# MMLU (5-shot)
python -m eval.mmlu.run_eval \
    --ntrain 0 \
    --data_dir data/eval/mmlu_${lang}/ \
    --save_dir results/mmlu_${lang}-0shot/"${model_name}"-0shot/ \
    --model_name_or_path "${model_path}" \
    --tokenizer_name_or_path "${model_path}" \
    --eval_batch_size 2 \
    --load_in_8bit --use_chat_format


lang=Portuguese
# MMLU (5-shot)
python -m eval.mmlu.run_eval \
    --ntrain 0 \
    --data_dir data/eval/mmlu_${lang}/ \
    --save_dir results/mmlu_${lang}-0shot/"${model_name}"-0shot/ \
    --model_name_or_path "${model_path}" \
    --tokenizer_name_or_path "${model_path}" \
    --eval_batch_size 2 \
    --load_in_8bit --use_chat_format


lang=Arabic
# MMLU (5-shot)
python -m eval.mmlu.run_eval \
    --ntrain 0 \
    --data_dir data/eval/mmlu_${lang}/ \
    --save_dir results/mmlu_${lang}-0shot/"${model_name}"-0shot/ \
    --model_name_or_path "${model_path}" \
    --tokenizer_name_or_path "${model_path}" \
    --eval_batch_size 2 \
    --load_in_8bit --use_chat_format


lang=Indonesian
# MMLU (5-shot)
python -m eval.mmlu.run_eval \
    --ntrain 0 \
    --data_dir data/eval/mmlu_${lang}/ \
    --save_dir results/mmlu_${lang}-0shot/"${model_name}"-0shot/ \
    --model_name_or_path "${model_path}" \
    --tokenizer_name_or_path "${model_path}" \
    --eval_batch_size 2 \
    --load_in_8bit --use_chat_format


lang=Hindi
# MMLU (5-shot)
python -m eval.mmlu.run_eval \
    --ntrain 0 \
    --data_dir data/eval/mmlu_${lang}/ \
    --save_dir results/mmlu_${lang}-0shot/"${model_name}"-0shot/ \
    --model_name_or_path "${model_path}" \
    --tokenizer_name_or_path "${model_path}" \
    --eval_batch_size 2 \
    --load_in_8bit --use_chat_format
