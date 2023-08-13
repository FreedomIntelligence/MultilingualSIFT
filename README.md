# Multilingual Supervised Instruction Fine-tuning

This repo aims to provide the data, models, evaluation benchmark for multilingual instruction fine-tuning.

## 📚 Data
We translate Alpaca-GPT4 and Evol-Instruct from English to languages using GPT-3.5 Turbo, where

* For Alpaca-GPT4, we directly translate the instructions and responses.
* For Evol-Instruct, we translate the instructions and use to generate the responses using the translated instructions.

| Language   | Alpaca-GPT4                                                                                 | Evol-instruct                                                                                 |ShareGPT                                                                                 |
|------------|---------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Chinese    | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-chinese)    | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-chinese)    |[[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/sharegpt-chinese)|
| Japanese   | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-japanese)   | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-japanese)   |[[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/sharegpt-japanese)|
| Korean     | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-korean)     | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-korean)     |[[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/sharegpt-korean)|
| German     | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-deutsch)    | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-deutsch)    |[[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/sharegpt-deutsch)|
| French     | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-french)     | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-french)     |[[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/sharegpt-french)|
| Italian    | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-italian)    | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-italian)    |[[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/sharegpt-italian)| 
| Arabic     | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-arabic)     | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-arabic)     |[[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/sharegpt-arabic)|
| Portuguese | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-portuguese) | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-portuguese) |[[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/sharegpt-portuguese)|
| Spanish    | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-spanish)    | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-spanish)    |[[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/sharegpt-spanish)|
| Hindi      | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-hindi)      | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-hindi)      |[[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/sharegpt-hindi)|
| Indonesian | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-indonesian) | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-indonesian) |[[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/sharegpt-indonesian)|

## 🤖 Models
### CLI Interation
```bash
python -m src.deploy.cli --model-path /path/to/weights/
```
For example, you can use the one fine-tuned on eight languages (`English`, `Chinese`, `French`, `Spanish`, `Portuguese`, `Arabic`, `Indonesian`, `Hindi`):
```bash
python -m src.deploy.cli --model-path FreedomIntelligence/phoenix-multiple-langs-v1
```

### Deployment
1. Launch a controller
```shell
python -m src.deploy.webapp.controller
```

2. Launch a model worker
```shell
python -m src.deploy.webapp.model_worker --model-path /path/to/weights/
```

3. Launch a gradio web server
```shell
python -m src.deploy.webapp.gradio_web_server
```
Now, you can open your browser and chat with a model.

### Training
Specify the `train_data_path` and `val_data_path` and then run
```shell
bash scripts/train.sh
```

## 💯 Evaluation Benchmark

### Evaluation Data

* We translate [MMLU](https://github.com/hendrycks/test) and [Vicuna-80](https://github.com/lm-sys/FastChat/blob/main/fastchat/llm_judge/data/vicuna_bench/question.jsonl) to languages above for evaluation.

| Language   | MMLU                                                                                 |
|------------|--------------------------------------------------------------------------------------|
| Chinese    | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Chinese)    |
| Japanese   | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Japanese)   |
| Korean     | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Korean)     |
| German     | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Deutsch)    |
| French     | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/MMLU_French)     |
| Italian    | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Italian)    |
| Arabic     | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Arabic)     |
| Portuguese | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Portuguese) |
| Spanish    | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Spanish)    |
| Hindi      | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Hindi)      |
| Indonesian | [[huggingface]](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Indonesian) |

### Evaluation

* For MMLU
```shell
bash scripts/eval_mmlu.sh ${LANGUAGE} ${MODEL_PATH} ${MODEL_ID}
```

* For Vicuna-80
```shell
bash scripts/eval_vicuna-80.sh ${LANGUAGE} ${MODEL_PATH} ${MODEL_ID}
```

## Citation

If you find this repository helpful, please cite the repository below.

```angular2
@software{Chen_MultilingualSIFT_Multilingual_Supervised_2023,
author = {Chen, Zhihong and Yan, Shuo and Liang, Juhao and Jiang, Feng and Wu, Xiangbo and Wang, Benyou},
month = jul,
title = {{MultilingualSIFT: Multilingual Supervised Instruction Fine-tuning}},
url = {https://github.com/FreedomIntelligence/MultilingualSIFT.git},
version = {0.1},
year = {2023}
}
```
