import subprocess
import time


def main():
    langs = ['Arabic', 'Chinese', 'English', 'French', 'Hindi', 'Indonesian', 'Portuguese', 'Spanish']
    models_1 = ["add_sharegpt_task_datasets_sc_ca_all_bloomz-7b1-mt"]
    models_2 = ["gpt35"]  # "gpt35"

    port = 5000
    records = []
    for model_1 in models_1:
        for lang in langs:
            for model_2 in models_2:
                time.sleep(5)
                port += 1
                cmd = f"python eval/human_eval/app.py {lang} {model_1} {model_2} {port}"
                print(f"61.241.103.34:{port} => ({lang}) {model_1} v.s. {model_2}")
                records.append(f"61.241.103.34:{port} => ({lang}) {model_1} v.s. {model_2}")
                child = subprocess.Popen(cmd, shell=True)
    with open("eval/human_eval/ip_records.txt", "wt") as fout:
        for record in records:
            fout.write(record + "\n")


if __name__ == '__main__':
    main()
