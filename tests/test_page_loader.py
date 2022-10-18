import os
import tempfile

import pytest
import requests
from page_loader.page_loader import (
    download,
    download_resources,
    generate_file_name,
    make_dir,
)

URL = {
    'css': 'https://site.com/blog/about/assets/styles.css',
    'html': 'https://site.com/blog/about',
    'image': 'https://site.com/photos/me.jpg',
    'js': 'https://site.com/assets/scripts.js',
}

NAME = {
    'css': 'site-com-blog-about-assets-styles.css',
    'dir': 'site-com-blog-about_files',
    'html': 'site-com-blog-about.html',
    'image': 'site-com-photos-me.jpg',
    'js': 'site-com-assets-scripts.js',
}

PATH_TO_FIXTURES = 'tests/fixtures'

PATH = {
    'css': os.path.join(PATH_TO_FIXTURES, NAME['dir'], NAME['css']),
    'dir': os.path.join(PATH_TO_FIXTURES, NAME['dir']),
    'html_before': os.path.join(PATH_TO_FIXTURES, NAME['dir'], NAME['html']),
    'html_after': os.path.join(PATH_TO_FIXTURES, NAME['html']),
    'image': os.path.join(PATH_TO_FIXTURES, NAME['dir'], NAME['image']),
    'js': os.path.join(PATH_TO_FIXTURES, NAME['dir'], NAME['js']),
}


@pytest.fixture
def fake_source(requests_mock):
    requests_mock.get(URL['html'], text=open(PATH['html_before'], 'r').read())
    requests_mock.get(URL['image'], content=open(PATH['image'], 'rb').read())
    requests_mock.get(URL['css'], content=open(PATH['css'], 'rb').read())
    requests_mock.get(URL['js'], content=open(PATH['js'], 'rb').read())


def test_generate_name():
    name_1 = os.path.join(os.getcwd(), NAME['html'])
    name_2 = os.path.join(os.getcwd(), PATH_TO_FIXTURES, NAME['html'])

    assert generate_file_name(URL['html'], '') + '.html' == name_1
    assert generate_file_name(URL['html'], PATH_TO_FIXTURES) + '.html' == name_2


def test_make_dir(fake_source):
    with tempfile.TemporaryDirectory() as tmpdirname:
        path_1 = make_dir(URL['html'], tmpdirname)
        path_2 = os.path.join(tmpdirname, NAME['dir'])
        assert path_1 == path_2


def test_download_resources(fake_source):
    with tempfile.TemporaryDirectory() as tmpdirname:
        path_1 = download_resources(URL['css'], tmpdirname)
        path_2 = os.path.join(tmpdirname, NAME['css'])
        assert path_1 == path_2

        with open(path_1, "rb") as file:
            assert file.read() == requests.get(URL['css']).content

    with tempfile.TemporaryDirectory() as tmpdirname:
        path_1 = download_resources(URL['html'], tmpdirname)
        path_2 = os.path.join(tmpdirname, NAME['html'])
        assert path_1 == path_2

        with open(path_1, encoding="utf-8") as file:
            assert file.read() == requests.get(URL['html']).text

    with tempfile.TemporaryDirectory() as tmpdirname:
        path_1 = download_resources(URL['image'], tmpdirname)
        path_2 = os.path.join(tmpdirname, NAME['image'])
        assert path_1 == path_2

        with open(path_1, "rb") as file:
            assert file.read() == requests.get(URL['image']).content

    with tempfile.TemporaryDirectory() as tmpdirname:
        path_1 = download_resources(URL['js'], tmpdirname)
        path_2 = os.path.join(tmpdirname, NAME['js'])
        assert path_1 == path_2

        with open(path_1, "rb") as file:
            assert file.read() == requests.get(URL['js']).content


def test_download(fake_source):
    with tempfile.TemporaryDirectory() as tmpdirname:
        path_received = download(URL['html'], tmpdirname)
        path_expected = os.path.join(tmpdirname, NAME['html'])
        assert path_received == path_expected

        assert len(os.listdir(tmpdirname)) == len(os.listdir(PATH_TO_FIXTURES))
        assert os.path.isfile(path_expected)
        assert os.path.dirname(os.path.join(tmpdirname, NAME['dir']))

        with open(path_received, encoding="utf-8") as file_received:
            with open(PATH['html_after'], encoding="utf-8") as file_expected:
                assert file_received.read() == file_expected.read()

        files_dir_received = os.listdir(os.path.join(tmpdirname, NAME['dir']))
        files_dir_expected = os.listdir(PATH['dir'])
        assert files_dir_received == files_dir_expected
