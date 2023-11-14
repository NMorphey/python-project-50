gendiff:
	poetry run gendiff
	
install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

reinstall: build publish package-install

pytest:
	poetry run pytest

test-coverage:
	coverage poetry run pytest
