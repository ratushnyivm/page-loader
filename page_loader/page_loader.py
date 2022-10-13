import os
import re
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

HEADERS = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/106.0.0.0 Safari/537.36'
}


def generate_file_name(url: str, output: str) -> str:
    delete_scheme = re.sub(r'((.*?)//)', '', url)

    split_url = os.path.splitext(delete_scheme)

    if split_url[1] in ['.html', '.png', '.jpg', '.jpeg', '.js', '.css']:
        delete_scheme = os.path.splitext(delete_scheme)[0]

    # Если нет расширения удаляет нужную часть url.
    # delete_extension = os.path.splitext(delete_scheme)[0]

    name = re.sub(r'[^\dA-Za-z]', '-', delete_scheme)

    new_path = name if output == os.getcwd() \
        else os.path.join(output, name)

    return os.path.abspath(new_path)


def download_html(url: str, file_path: str) -> str:
    req = requests.get(url, headers=HEADERS)

    file_name = f'{generate_file_name(url, file_path)}.html'

    with open(file_name, 'w', encoding="utf-8") as f:
        f.write(req.text)

    return file_name


def make_dir(url: str, file_path: str) -> str:
    dir_name = f'{generate_file_name(url, file_path)}_files'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    return dir_name


def download_image(url: str, file_path: str) -> str:
    req = requests.get(url, headers=HEADERS)

    file_name = f'{generate_file_name(url, file_path)}.jpg'

    with open(file_name, 'wb') as x:
        x.write(req.content)

    return file_name


def download(url: str, file_path: str) -> str:
    path_to_html = download_html(url, file_path)
    print(f'Путь до html-файла: {path_to_html}')

    path_to_dir = make_dir(url, file_path)
    print(f'Путь до папки с файлами: {path_to_dir}')

    relative_path_to_dir = f'./{os.path.split(path_to_dir)[1]}'
    print(f'Относительный путь до папки с файлами: {relative_path_to_dir}')

    print('---------------------------------------')

    with open(path_to_html, encoding="utf-8") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    for image in soup.find_all('img'):

        if urlparse(url).netloc == urlparse(image.attrs.get('src')).netloc \
                or not len(urlparse(image.attrs.get('src')).netloc):

            print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

            print(image)

            image_url = urljoin(url, image.attrs.get('src'))
            print(image_url)

            path_to_img = download_image(image_url, path_to_dir)
            print(path_to_img)

            name_img = os.path.split(path_to_img)[1]
            print(name_img)

            relative_path_to_img = os.path.join(
                relative_path_to_dir,
                name_img
            )
            print(relative_path_to_img)

            image['src'] = relative_path_to_img
            print(image)

    with open(path_to_html, 'w', encoding="utf-8") as f:
        f.write(soup.prettify())

    return path_to_html
