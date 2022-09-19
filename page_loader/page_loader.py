import os
import re

import requests


def generate_file_name(url: str, output: str) -> str:
    delete_scheme = re.sub(r'((.*?)//)', '', url)
    delete_extension = os.path.splitext(delete_scheme)[0]

    name = re.sub(r'[^\dA-Za-z]', '-', delete_extension)
    full_name = f'{name}.html'

    new_path = full_name if output == os.getcwd() \
        else os.path.join(output, full_name)

    return os.path.abspath(new_path)


def download(url, file_path):
    resp = requests.get(url)

    file_name = generate_file_name(url, file_path)

    with open(file_name, 'w', encoding="utf-8") as f:
        f.write(resp.text)

    return file_name
