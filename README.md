<div align="center">

# Page Loader

[![hexlet-check](https://github.com/ratushnyyvm/page-loader/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ratushnyyvm/page-loader/actions/workflows/hexlet-check.yml)
[![lint and test](https://github.com/ratushnyyvm/page-loader/actions/workflows/page-loader-CI.yml/badge.svg)](https://github.com/ratushnyyvm/page-loader/actions/workflows/gendiff-CI.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/7511786d12e08e3d6983/maintainability)](https://codeclimate.com/github/ratushnyyvm/page-loader/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/7511786d12e08e3d6983/test_coverage)](https://codeclimate.com/github/ratushnyyvm/page-loader/test_coverage)

</div>

---

## Description

PageLoader is a command line utility that downloads pages from the internet and stores them on your computer. Along with the page it downloads all the resources (images, styles and js) allowing you to open the page without the Internet.

---

## Dependencies

| Tool              | Version         |
|-------------------|-----------------|
| python            | "^3.8.1"        |
| requests          | "^2.28.1"       |
| beautifulsoup4    | "^4.11.1"       |
| progress          | "^1.6"          |

---

## Installation

Before installation, make sure that you have [Python](https://www.python.org/) and [Poetry](https://python-poetry.org/) installed.

1. Clone the repository to your computer `git clone https://github.com/ratushnyyvm/page-loader.git`
2. Go to the project folder `cd page-loader`
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
