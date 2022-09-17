import os
from page_loader.page_loader import generate_file_name


URL = 'https://ru.hexlet.io/courses'
NAME = 'ru-hexlet-io-courses.html'
DIR_PATH = './tests'

FILE_NAME_1 = os.path.join(os.getcwd(), NAME)
FILE_NAME_2 = os.path.join(os.getcwd(), DIR_PATH[2:], NAME)


def test_generate_file_name():
    assert generate_file_name(URL, '') == FILE_NAME_1
    assert generate_file_name(URL, DIR_PATH) == FILE_NAME_2
