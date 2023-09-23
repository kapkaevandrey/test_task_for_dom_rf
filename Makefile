SHELL := /bin/bash
pip:
	poetry shell && poetry install

cleaning:
	find . -name '*.pyc' | xargs rm -rf
	find . -name '*__pycache__' | xargs rm -rf
	find . -name '*.cache' | xargs rm -rf
	rm -r .pytest_cache 2>/dev/null || true
	rm -r htmlcov 2>/dev/null || true
	rm -r .coverage 2>/dev/null || true

isort:
	./lint isort

black:
	./lint black

lint: cleaning isort black
