install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip uninstall hexlet-code -y
	python3 -m pip install --user dist/*.whl

setup: install build package-install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
