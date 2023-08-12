export OMP_NUM_THREADS=1
export PYTHONPATH=${PWD}

model_name_or_path=bigscience/bloomz-7b1-mt
model_max_length=1024
train_data_path=<PATH-1>,<PATH-2>,...,<PATH-n>
val_data_path=<PATH-1>,<PATH-2>,...,<PATH-n>

run_name=Phoenix-Multilingual
output_dir=checkpoints/${run_name}/

torchrun \
  --nnodes=1 \
  --nproc_per_node=8 \
  --master_port=12375 \
  src/main/train.py \
  --model_name_or_path ${model_name_or_path} \
  --model_max_length ${model_max_length} \
  --train_data_path ${train_data_path} \
  --val_data_path ${val_data_path} \
  --output_dir ${output_dir} \
  --bf16 True \
  --num_train_epochs 3 \
  --per_device_train_batch_size 8 \
  --per_device_eval_batch_size 4 \
  --gradient_accumulation_steps 4 \
  --save_strategy "steps" \
  --save_steps 500 \
  --evaluation_strategy "steps" \
  --eval_steps 500 \
  --save_total_limit 5 \
  --learning_rate 2e-5 \
  --weight_decay 0. \
  --warmup_ratio 0.03 \
  --lr_scheduler_type "cosine" \
  --logging_steps 1 \
  --fsdp "full_shard auto_wrap" \
  --fsdp_transformer_layer_cls_to_wrap 'BloomBlock' \
  --tf32 True \
  --gradient_checkpointing True \
  --run_name ${run_name}
