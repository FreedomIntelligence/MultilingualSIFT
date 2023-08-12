import json
import os
import pandas as pd
from collections import defaultdict


def main():
    results = defaultdict(dict)
    review_dir = "eval/vicuna_eval/gpt4_api_outputs/"
    for lang in os.listdir(review_dir):
        for model in os.listdir(os.path.join(review_dir, lang)):
            model_name = model.split("_vs._")[1]
            lang_name = lang.split("_")[-1]
            data = json.load(open(os.path.join(review_dir, lang, model, "random avg", "metrics.json")))
            results[model_name][lang_name] = data["Total"][model_name]["Avg Score"]["AVG 1"] / \
                                             data["Total"]["gpt35"]["Avg Score"]["AVG 1"]
    results = (pd.DataFrame(results) * 100).round(2).T
    import pdb
    pdb.set_trace()


if __name__ == '__main__':
    main()
