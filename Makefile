.PHONY: build test test-local run

build:
	docker build -t challenge/dev --target dev .
	docker build -t challenge --target prod .

test : build
	docker run challenge/dev poetry run pylint src tests
	docker run challenge/dev poetry run mypy src tests
	docker run challenge/dev poetry run pytest -vv

test-local :
	poetry run pylint src tests
	poetry run mypy src tests
	poetry run pytest -vv

run : build
	docker run challenge
