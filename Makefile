.PHONY: docs
init:
  pip install -r requirements-dev.txt
test:
  tox -p
ci:
  pytest tests --junitxml=report.xml

coverage:
  pytest --cov-config .coveragerc --verbose --cov-report term --cov-report xml --cov=requests tests
