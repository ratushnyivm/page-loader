import requests


def download(url, file_path=None):
    r = requests.get(url)
    return r.text


print(download('https://ru.hexlet.io/courses'))
