import argparse
import copy
import json
import os

import ray
import shortuuid
import torch
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM

from src.utils import get_default_conv_template


def run_eval(model_path, model_id, question_file, answer_file, num_gpus):
    ques_jsons = []
    with open(os.path.expanduser(question_file), "r") as ques_file:
        for line in ques_file:
            ques_jsons.append(line)

    chunk_size = len(ques_jsons) // num_gpus
    ans_handles = []
    for i in range(0, len(ques_jsons), chunk_size):
        ans_handles.append(
            get_model_answers.remote(
                model_path, model_id, ques_jsons[i: i + chunk_size]
            )
        )

    ans_jsons = []
    for ans_handle in ans_handles:
        ans_jsons.extend(ray.get(ans_handle))

    os.makedirs(os.path.dirname(answer_file), exist_ok=True)
    with open(os.path.expanduser(answer_file), "w", encoding="utf-8") as ans_file:
        for line in ans_jsons:
            ans_file.write(json.dumps(line, ensure_ascii=False) + "\n")


@ray.remote(num_gpus=1)
@torch.inference_mode()
def get_model_answers(model_path, model_id, question_jsons):
    model_path = os.path.expanduser(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, low_cpu_mem_usage=True, torch_dtype=torch.float16).cuda()

    ans_jsons = []
    for i, line in enumerate(tqdm(question_jsons)):
        ques_json = json.loads(line)
        idx = ques_json["question_id"]
        qs = ques_json["text"]
        conv = copy.deepcopy(get_default_conv_template(model_id))
        conv.append_message(conv.roles[0], qs)
        conv.append_message(conv.roles[1], None)
        prompt = conv.get_prompt()
        input_ids = tokenizer([prompt]).input_ids
        output_ids = model.generate(
            torch.as_tensor(input_ids).cuda(),
            do_sample=True,
            temperature=0.7,
            max_new_tokens=1024
        )
        output_ids = output_ids[0][len(input_ids[0]):]
        outputs = tokenizer.decode(output_ids, skip_special_tokens=True).strip()

        ans_id = shortuuid.uuid()
        ans_jsons.append(
            {
                "question_id": idx,
                "text": outputs,
                "answer_id": ans_id,
                "model_id": model_id,
                "metadata": {},
            }
        )
        print(f'Q: {prompt}')
        print(f'A: {outputs}')

    return ans_jsons


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", type=str, required=True)
    parser.add_argument("--model-id", type=str, required=True)
    parser.add_argument("--question-file", type=str, required=True)
    parser.add_argument("--answer-file", type=str, default="answer.jsonl")
    parser.add_argument("--num-gpus", type=int, default=1)
    args = parser.parse_args()

    ray.init()
    run_eval(
        args.model_path,
        args.model_id,
        args.question_file,
        args.answer_file,
        args.num_gpus,
    )
