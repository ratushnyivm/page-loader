import os
import tempfile

import pytest
import requests
from page_loader.page_loader import (
    download_html,
    download_image,
    generate_file_name,
    make_dir,
)

URL = 'https://site.com/blog/about'
URL_TO_IMAGE = 'https://site.com/photos/me'

NAME = 'site-com-blog-about'
NAME_TO_IMAGE = 'site-com-photos-me.jpg'
DIR_PATH = './tests'


def test_generate_name():
    name_1 = os.path.join(os.getcwd(), NAME)
    name_2 = os.path.join(os.getcwd(), DIR_PATH[2:], NAME)

    assert generate_file_name(URL, '') == name_1
    assert generate_file_name(URL, DIR_PATH) == name_2


@pytest.fixture
def fake_source(requests_mock):
    path_to_html_before = 'tests/fixtures/site-com-blog-about_files/site-com-blog-about.html' # noqa
    path_to_image = 'tests/fixtures/site-com-blog-about_files/site-com-photos-me.jpg' # noqa

    requests_mock.get(URL, text=open(path_to_html_before, 'r').read())
    requests_mock.get(URL_TO_IMAGE, content=open(path_to_image, 'rb').read())


def test_download_html(fake_source):
    with tempfile.TemporaryDirectory() as tmpdirname:
        path_1 = download_html(URL, tmpdirname)
        path_2 = os.path.join(tmpdirname, f'{NAME}.html')
        assert path_1 == path_2

        with open(path_1, encoding="utf-8") as file:
            assert file.read() == requests.get(URL).text


def test_make_dir(fake_source):
    with tempfile.TemporaryDirectory() as tmpdirname:
        path_1 = make_dir(URL, tmpdirname)
        path_2 = os.path.join(tmpdirname, f'{NAME}_files')
        assert path_1 == path_2


def test_download_image(fake_source):
    with tempfile.TemporaryDirectory() as tmpdirname:
        path_1 = download_image(URL_TO_IMAGE, tmpdirname)
        path_2 = os.path.join(tmpdirname, f'{NAME_TO_IMAGE}')
        assert path_1 == path_2
