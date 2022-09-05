import requests
import re


def convert_name(url: str) -> str:
    delete_scheme = re.sub(r'((.*?)//)', '', url)
    new_url = re.sub(r'[^\dA-Za-z]', '-', delete_scheme)
    return new_url


def download(url, file_path=None):
    r = requests.get(url)
    return r.text


# print(download('https://ru.hexlet.io/courses'))
print(convert_name('https://ru.hexlet.io/courses'))
