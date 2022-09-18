import os
import requests_mock
from page_loader.page_loader import generate_file_name
from page_loader.page_loader import download


URL = 'https://ru.hexlet.io/courses'
NAME = 'ru-hexlet-io-courses.html'
DIR_PATH = './tests'

FILE_NAME_1 = os.path.join(os.getcwd(), NAME)
FILE_NAME_2 = os.path.join(os.getcwd(), DIR_PATH[2:], NAME)


def test_generate_file_name():
    assert generate_file_name(URL, '') == FILE_NAME_1
    assert generate_file_name(URL, DIR_PATH) == FILE_NAME_2


def test_download():
    with open('tests/fixtures/ru-hexlet-io-courses_test.html') as f:
        data = f.read()

    with requests_mock.Mocker() as m:
        m.get(URL, text=data)
        download(URL, './tests/fixtures')

    with open('tests/fixtures/ru-hexlet-io-courses.html') as x:
        data_before = x.read()

    assert data_before == data
