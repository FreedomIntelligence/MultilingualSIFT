import csv
import json
import os
import random
import sys

import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def generate_comparisons():
    read_jsonl = lambda x: sorted([json.loads(line) for line in open(x)], key=lambda x: int(x["question_id"]))
    questions = read_jsonl(os.path.join("eval", "vicuna_eval", "questions", f"questions_{lang}.jsonl"))
    answers_1 = read_jsonl(os.path.join("eval", "vicuna_eval", "answers", lang, f"{model_1}.jsonl"))
    answers_2 = read_jsonl(os.path.join("eval", "vicuna_eval", "answers", lang, f"{model_2}.jsonl"))

    data = []
    for question, sample_1, sample_2 in zip(questions, answers_1, answers_2):
        assert int(question["question_id"]) == int(sample_1["question_id"]) == int(sample_2["question_id"])
        q = question["text"]
        a1 = sample_1["text"]
        a2 = sample_2["text"]
        rand = random.random()
        if rand < 0.5:
            data.append((q, a1, a2, False))
        else:
            data.append((q, a2, a1, True))

    df = pd.DataFrame({"Question": [s[0] for s in data],
                       "Answer 1": [s[1] for s in data],
                       "Answer 2": [s[2] for s in data],
                       "Shuffle": [s[3] for s in data]})
    df.to_csv(data_file)


def read_data():
    with open(data_file, 'r') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data


def write_output(data):
    id = 0
    while os.path.exists(os.path.join("eval", "human_eval", "outputs", f"{lang}_{model_1}_{model_2}_{id}.csv")):
        id = id + 1
    output_file = os.path.join("eval", "human_eval", "outputs", f"{lang}_{model_1}_{model_2}_{id}.csv")

    with open(output_file, 'w', newline='', encoding="utf-8") as f:
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


@app.route('/')
def index():
    data = read_data()
    return render_template('index.html', data=data)


@app.route('/save', methods=['POST'])
def save():
    data = read_data()
    for row in data:
        question_id = str(row['Question'])
        result = request.form.get(question_id)
        row['Result'] = result
    write_output(data)
    return redirect(url_for('index'))


if __name__ == '__main__':
    lang = sys.argv[1]  # "Chinese"
    model_1 = sys.argv[2]  # "add_sharegpt_task_datasets_sc_ca_all_bloomz-7b1-mt"
    model_2 = sys.argv[3]  # "gpt35"
    port = sys.argv[4]  # 5000

    os.makedirs(os.path.join("eval", "human_eval", "inputs"), exist_ok=True)
    os.makedirs(os.path.join("eval", "human_eval", "outputs"), exist_ok=True)
    data_file = os.path.join("eval", "human_eval", "inputs", f"{lang}_{model_1}_{model_2}.csv")

    generate_comparisons()

    app.run(host='0.0.0.0', port=port, debug=True)
