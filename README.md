# MultilingualSIFT: Multilingual Supervised Instruction Fine-tuning

## Dataset
| Target Language | Alpaca-gpt4                                                                               | Evol-instruct                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Chinese         | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-chinese)    | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-chinese)    
| Japanese        | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-japanese)   | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-japanese)   |
| Korean          | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-korean)     | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-korean)     |
| German          | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-deutsch)    | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-deutsch)    |
| French          | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-french)     | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-french)     |
| Italian         | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-italian)    | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-italian)    |
| Arabic          | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-arabic)     | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-arabic)     |
| Portuguese      | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-portuguese) | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-portuguese) |
| Spanish         | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-spanish)    | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-spanish)    |
| Hindi           | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-hindi)      | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-hindi)      |
| Indonesian      | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/alpaca-gpt4-indonesian) | [huggingface](https://huggingface.co/datasets/FreedomIntelligence/evol-instruct-indonesian) |

We translate Alpaca-GPT4 and Evol-Instruct from English to languages above. For Alpaca-GPT4, we directly translate the instructions and responses; For Evol-Instruct, we translate the instructions and use GPT-3.5 to generate the responses using the translated instructions. These translated datasets are used in the supervised fine-tuning period to investigate whether multilingual training  is beneficial to a specific language in the supervised instruction fine-tuning(SIFT) stage and other factors which may be helpful to the multilingual performance of LLM in SIFT stage.

Besides, we use GPT-3.5 translate [MMLU dataset](https://github.com/hendrycks/test) to languages above for evaluation. The translated MMLU datasets can be found in [huggingface](https://huggingface.co/FreedomIntelligence)




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
