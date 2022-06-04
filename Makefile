.PHONY: docs
init:
	pip install -r requirements-dev.txt
test:
	tox -p
ci:
	pytest tests --junitxml=report.xml

coverage:
	pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=requests tests

docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"

