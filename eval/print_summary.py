import json
import os
import re
from collections import defaultdict

import pandas as pd

langs = ["english", "french", "spanish", "portuguese", "hindi", "deutsch", "italian", "chinese", "arabic", "indonesian",
         "korean", "japanese"]

keys = {
    "bbh": "average_exact_match",
    "codex_humaneval": "pass@10",
    # "tydiqa": "f1",
    "gsm": "exact_match",
    "mgsm": "average",
    "mmlu": "average_acc",
    "mmlu_Arabic": "average_acc",
    "mmlu_Chinese": "average_acc",
    "mmlu_French": "average_acc",
    "mmlu_Hindi": "average_acc",
    "mmlu_Indonesian": "average_acc",
    "mmlu_Portuguese": "average_acc",
    "mmlu_Spanish": "average_acc",
    "mmlu-0shot": "average_acc",
    "mmlu_Arabic-0shot": "average_acc",
    "mmlu_Chinese-0shot": "average_acc",
    "mmlu_French-0shot": "average_acc",
    "mmlu_Hindi-0shot": "average_acc",
    "mmlu_Indonesian-0shot": "average_acc",
    "mmlu_Portuguese-0shot": "average_acc",
    "mmlu_Spanish-0shot": "average_acc",
}


def main():
    result_dir = "results"

    results = defaultdict(dict)
    for dataset in os.listdir(result_dir):
        for model in os.listdir(os.path.join(result_dir, dataset)):
            try:
                data = json.load(open(os.path.join(result_dir, dataset, model, "metrics.json")))
                model = re.sub("-\dshot", "", model)
                model = re.sub("-cot", "", model)
                model = re.sub("-goldp", "", model)
                # if dataset == "tydiqa":
                #     results[dataset][model] = data["average"]["f1"] / 100
                #     scores = {k: v["f1"] for k, v in data.items() if k in langs}
                #     for k, v in scores.items():
                #         results[f"{dataset}-{k}"][model] = v / 100
                #     results[f"{dataset}-x"][model] = sum([v / 100 for k, v in scores.items()]) / len(scores)
                # else:
                #     results[dataset][model] = data[keys[dataset]]

                if dataset == "tydiqa":
                    results[dataset][model] = data["average"]["f1"] / 100
                    scores = {k: v["f1"] for k, v in data.items() if k in langs}
                    results[f"{dataset}-x"][model] = sum([v / 100 for k, v in scores.items()]) / len(scores)
                else:
                    results[dataset][model] = data[keys[dataset]]

            except FileNotFoundError:
                print(f'{dataset}: {model}')
    results = pd.DataFrame(results)
    results["avg"] = results.mean(axis=1)
    results = results.sort_values(by="avg", ascending=False) * 100
    print(results.round(2))
    import pdb
    pdb.set_trace()
    # print(results["add_sharegpt_sc_ca_all_bloom-7b1"].round(2))
    # print(results["add_sharegpt_task_datasets_sc_ca_all_bloomz-7b1-mt"].round(2))


if __name__ == '__main__':
    main()
