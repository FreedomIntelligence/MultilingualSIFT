# MultilingualSIFT: Multilingual Supervised Instruction Fine-tuning

## Multilingual Instruction Data
### Data Summary
| Target Language | Alpaca-gpt4                                                                               | Evol-instruct             | MMLU                 |
|-----------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Chinese         | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-chinese)    | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-chinese) | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Chinese) |
| Japanese        | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-japanese)   | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-japanese)   | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Japanese) |
| Korean          | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-korean)     | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-korean)     | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Korean) |
| German          | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-deutsch)    | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-deutsch)    | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Deutsch) |
| French          | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-french)     | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-french)     | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/MMLU_French) |
| Italian         | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-italian)    | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-italian)    | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Italian) |
| Arabic          | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-arabic)     | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-arabic)     | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Arabic) |
| Portuguese      | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-portuguese) | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-portuguese) | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Portuguese) |
| Spanish         | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-spanish)    | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-spanish)    | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Spanish) |
| Hindi           | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-hindi)      | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-hindi)      | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Hindi) |
| Indonesian      | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-indonesian) | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-indonesian) | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/MMLU_Indonesian) |

### Data Construction Process
We translate Alpaca-GPT4 and Evol-Instruct from English to languages using GPT-3.5 Turbo, where
* For Alpaca-GPT4, we directly translate the instructions and responses.  
* For Evol-Instruct, we translate the instructions and use  to generate the responses using the translated instructions.  
* We also translate [MMLU dataset](https://github.com/hendrycks/test) to languages above for evaluation.

These translated Alpaca-GPT4 and Evol-Instruct datasets are used in the supervised fine-tuning period to investigate whether multilingual training is beneficial to a specific language in the supervised instruction fine-tuning(SIFT) stage and other factors which may be helpful to the multilingual performance of LLM in the SIFT stage.

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
