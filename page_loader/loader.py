import os
import re
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from page_loader.logger import logger
from progress.bar import ChargingBar


def generate_file_name(url: str, output: str) -> str:
    extensions_list = ['.html', '.png', '.jpg', '.jpeg', '.js', '.css']
    regex_search_scheme = r'((.*?)//)'
    regex_search_symbols = r'[^\dA-Za-z]'

    url_without_scheme = re.sub(regex_search_scheme, '', url)
    split_url = os.path.splitext(url_without_scheme)

    if split_url[1] in extensions_list:
        name = re.sub(regex_search_symbols, '-', split_url[0]) + split_url[1]
    else:
        name = re.sub(regex_search_symbols, '-', url_without_scheme)

    new_path = name if output == os.getcwd() else os.path.join(output, name)

    return os.path.abspath(new_path)


def make_dir(url: str, file_path: str) -> str:
    name = f'{os.path.splitext(generate_file_name(url, file_path))[0]}_files'
    if not os.path.exists(name):
        os.mkdir(name)

    logger.debug(f'Создана папка по адресу: {name}')

    return name


def download_resources(url: str, file_path: str) -> str:
    req = requests.get(url)
    file_name = generate_file_name(url, file_path)
    extension = os.path.splitext(file_name)[1]

    if extension == '.html' or extension == '':
        file_name += '.html'
        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(req.text)
    else:
        with open(file_name, 'wb') as x:
            x.write(req.content)

    return file_name


def change_tags(
        soup_obj: BeautifulSoup,
        url: str,
        tag_name: str,
        attribute: str,
        path_to_dir: str,
        relative_path_to_dir: str,
):
    tags = soup_obj.find_all(tag_name)
    for tag in tags:
        if urlparse(url).netloc == urlparse(tag.attrs.get(attribute)).netloc \
                or not len(urlparse(tag.attrs.get(attribute)).netloc):
            tag_url = urljoin(url, tag.attrs.get(attribute))
            path_to_tag = download_resources(tag_url, path_to_dir)
            name_tag = os.path.split(path_to_tag)[1]
            relative_path_to_tag = os.path.join(
                relative_path_to_dir,
                name_tag
            )
            tag[attribute] = relative_path_to_tag


def download(url, file_path):

    logger.info(f'requested url: {url}')
    logger.info(f'output path: {file_path}')

    path_to_html = download_resources(url, file_path)
    path_to_dir = make_dir(url, file_path)
    relative_path_to_dir = f'{os.path.basename(path_to_dir)}'

    with open(path_to_html, encoding="utf-8") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    dict_tags = {
        'tag_name': ['img', 'link', 'script'],
        'attribute': ['src', 'href', 'src'],
    }

    bar = ChargingBar('Downloading:', max=len(dict_tags['tag_name']))

    for item in range(len(dict_tags['tag_name'])):
        change_tags(
            soup_obj=soup,
            url=url,
            tag_name=dict_tags['tag_name'][item],
            attribute=dict_tags['attribute'][item],
            path_to_dir=path_to_dir,
            relative_path_to_dir=relative_path_to_dir
        )
        bar.next()
    bar.finish()

    with open(path_to_html, 'w', encoding="utf-8") as f:
        f.write(soup.prettify())

    logger.info(f'Page was downloaded as {path_to_html}\n')

    return path_to_html
