# PageLoader

[![Actions Status](https://github.com/ratushnyyvm/python-project-51/workflows/hexlet-check/badge.svg)](https://github.com/ratushnyyvm/python-project-51/actions)
[![lint and test](https://github.com/ratushnyyvm/python-project-51/actions/workflows/page-loader-CI.yml/badge.svg)](https://github.com/ratushnyyvm/python-project-51/actions/workflows/page-loader-CI.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/25e839a095d958578765/maintainability)](https://codeclimate.com/github/ratushnyyvm/python-project-51/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/25e839a095d958578765/test_coverage)](https://codeclimate.com/github/ratushnyyvm/python-project-51/test_coverage)

---

## Description

PageLoader is a command line utility that downloads pages from the internet and stores them on your computer. Along with the page it downloads all the resources (images, styles and js) allowing you to open the page without the Internet.

---

## Installation

1. Clone the repository to your computer `git clone https://github.com/ratushnyyvm/python-project-51.git`
2. Go to the project folder `cd python-project-lvl2`
3. Install the program `make setup`

---

## Usage

### Cli-utility

``` bash
$ page-loader -h
usage: page-loader [-h] [-o OUTPUT] url

Downloads web-pages and save locally

positional arguments:
  url

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output dir (default: current directory)
```

### Library

``` python
from page_loader import download

file_path = download('https://ru.hexlet.io/courses', '/var/tmp')
print(file_path)  # => '/var/tmp/ru-hexlet-io-courses.html'
```

---

## Demonstration

[![asciicast](https://asciinema.org/a/FMc5h0KycTS4oQhH7NdpUwuOw.svg)](https://asciinema.org/a/FMc5h0KycTS4oQhH7NdpUwuOw)

---

The third training project from ["Python developer" course](https://ru.hexlet.io/programs/python)