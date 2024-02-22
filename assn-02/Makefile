.PHONY: help
.DEFAULT_GOAL := help

help:
	python -m pos --help

install: ## Install requirements
	pip install -r requirements.txt

format: ## Run code formatters
	isort pos
	black pos

lint: ## Run code linters
	isort --check pos
	black --check pos
	flake8 pos
	mypy pos
