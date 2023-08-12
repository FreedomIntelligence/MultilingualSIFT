# Hyper-parameters
model_name=${1}  # bloom-560m
model_dir=models_phoenix_ii
model_path=${model_dir}/${model_name}/

# TydiQA (1-shot, GP)
python -m eval.tydiqa.run_eval \
   --data_dir data/eval/tydiqa/ \
   --n_shot 1 \
   --max_num_examples_per_lang 100 \
   --max_context_length 512 \
   --save_dir results/tydiqa/"${model_name}"-goldp-1shot \
   --model "${model_path}" \
   --tokenizer "${model_path}" \
   --eval_batch_size 20 \
   --load_in_8bit

# MMLU (5-shot)
python -m eval.mmlu.run_eval \
    --ntrain 5 \
    --data_dir data/eval/mmlu \
    --save_dir results/mmlu/"${model_name}"-5shot/ \
    --model_name_or_path "${model_path}" \
    --tokenizer_name_or_path "${model_path}" \
    --eval_batch_size 2 \
    --load_in_8bit

# GSM (8-shot, cot)
python -m eval.gsm.run_eval \
   --data_dir data/eval/gsm/ \
   --max_num_examples 200 \
   --save_dir results/gsm/"${model_name}"-8shot-cot \
   --model "${model_path}" \
   --tokenizer "${model_path}" \
   --eval_batch_size 20 \
   --n_shot 8 \
   --load_in_8bit

# MGSM (8-shot, cot)
python -m eval.mgsm.run_eval \
    --data_dir data/eval/mgsm/ \
    --max_num_examples_per_lang 40 \
    --save_dir results/mgsm/"${model_name}"-8shot-cot \
    --model "${model_path}" \
    --tokenizer "${model_path}" \
    --eval_batch_size 4 \
    --n_shot 8 \
    --load_in_8bit


# BBH (3-shot?, cot)
 python -m eval.bbh.run_eval \
     --data_dir data/eval/bbh \
     --save_dir results/bbh/"${model_name}"-cot/ \
     --model "${model_path}" \
     --tokenizer "${model_path}" \
     --eval_batch_size 10 \
     --max_num_examples_per_task 40 \
     --load_in_8bit

# Codex-Eval (P@10)
python -m eval.codex_humaneval.run_eval \
   --data_file data/eval/codex_humaneval/HumanEval.jsonl.gz \
   --eval_pass_at_ks 1 5 10 \
   --unbiased_sampling_size_n 10 \
   --temperature 0.1 \
   --save_dir results/codex_humaneval/"${model_name}" \
   --model "${model_path}" \
   --tokenizer "${model_path}" \
   --eval_batch_size 32 \
   --load_in_8bit