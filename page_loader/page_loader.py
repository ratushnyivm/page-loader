import os
import requests
import re


def generate_file_name(url: str, output: str) -> str:
    delete_scheme = re.sub(r'((.*?)//)', '', url)
    delete_extension = os.path.splitext(delete_scheme)[0]
    new_url = re.sub(r'[^\dA-Za-z]', '-', delete_extension)
    return new_url if output == os.getcwd() else os.path.join(output, new_url)


def download(url, file_path):
    r = requests.get(url)

    file_name = f'{generate_file_name(url, file_path)}.html'

    with open(file_name, 'w', encoding="utf-8") as x:
        x.write(r.text)

    return file_name
