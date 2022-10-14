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


def download_link(url, file_path):
    req = requests.get(url, headers=HEADERS)
    file_name = f'{generate_file_name(url, file_path)}.css'
    with open(file_name, 'wb') as x:
        x.write(req.content)

    return file_name


def download_script(url, file_path):
    req = requests.get(url, headers=HEADERS)
    file_name = f'{generate_file_name(url, file_path)}.js'
    with open(file_name, 'wb') as x:
        x.write(req.content)

    return file_name


def download(url, file_path):
    # Скачиваю html-страницу.
    path_to_html = download_html(url, file_path)
    print(f'Путь до html-файла: {path_to_html}')

    # Создаю папку с ресурсами.
    path_to_dir = make_dir(url, file_path)
    print(f'Путь до папки с файлами: {path_to_dir}')

    # Извлекаю относительный путь до папки.
    relative_path_to_dir = f'./{os.path.split(path_to_dir)[1]}'
    print(f'Относительный путь до папки с файлами: {relative_path_to_dir}')

    print('---------------------------------------')

    # Сохраняю содержимое html-страницы в переменную.
    with open(path_to_html, encoding="utf-8") as f:
        html_doc = f.read()

    # Создаю объект супа.
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Прохожу циклом по всем тегам <img>.
    for image in soup.find_all('img'):

        # Проверяю соответствие доменов.
        if urlparse(url).netloc == urlparse(image.attrs.get('src')).netloc \
                or not len(urlparse(image.attrs.get('src')).netloc):

            print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')

            print(image)

            # Создаю абсолютную ссылку.
            image_url = urljoin(url, image.attrs.get('src'))
            print(image_url)

            # Скачиваю файл.
            path_to_img = download_image(image_url, path_to_dir)
            print(path_to_img)

            # Извлекаю имя файла.
            name_img = os.path.split(path_to_img)[1]
            print(name_img)

            # Создаю относительный путь до файла.
            relative_path_to_img = os.path.join(
                relative_path_to_dir,
                name_img
            )
            print(relative_path_to_img)

            # Изменяю ссылку на файл.
            image['src'] = relative_path_to_img
            print(image)

    for link in soup.find_all('link'):

        if urlparse(url).netloc == urlparse(link.attrs.get('href')).netloc \
                or not len(urlparse(link.attrs.get('href')).netloc):

            link_url = urljoin(url, link.attrs.get('href'))

            if link_url.endswith('.css'):
                path_to_link = download_link(link_url, path_to_dir)
                name_link = os.path.split(path_to_link)[1]
                relative_path_to_link = os.path.join(
                    relative_path_to_dir,
                    name_link
                )
                link['href'] = relative_path_to_link

            else:
                path_to_link = download_html(link_url, path_to_dir)
                name_link = os.path.split(path_to_link)[1]
                relative_path_to_link = os.path.join(
                    relative_path_to_dir,
                    name_link
                )
                link['href'] = relative_path_to_link

    for script in soup.find_all('script'):

        if urlparse(url).netloc == urlparse(script.attrs.get('src')).netloc \
                or not len(urlparse(script.attrs.get('src')).netloc):

            script_url = urljoin(url, script.attrs.get('src'))
            path_to_script = download_script(script_url, path_to_dir)
            name_script = os.path.split(path_to_script)[1]
            relative_path_to_script = os.path.join(
                relative_path_to_dir,
                name_script
            )
            script['src'] = relative_path_to_script

    # Записываю измененный html.
    with open(path_to_html, 'w', encoding="utf-8") as f:
        f.write(soup.prettify())

    return path_to_html
