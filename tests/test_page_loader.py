from page_loader.page_loader import generate_file_name


URL = 'https://ru.hexlet.io/courses'
FILE_NAME_1 = '/home/rvm/python-project-51/ru-hexlet-io-courses.html'
FILE_NAME_2 = '/home/rvm/python-project-51/tests/ru-hexlet-io-courses.html'


def test_generate_file_name():
    assert generate_file_name(URL, '') == FILE_NAME_1
    assert generate_file_name(URL, './tests') == FILE_NAME_2
