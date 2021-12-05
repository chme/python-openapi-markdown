REQUIREMENTS_TXT=requirements_dev.txt

.PHONY: test
test: venv
	$(VENV)/pytest

.PHONY: lint
lint: venv
	$(VENV)/flake8 --exclude=.tox,.venv

.PHONY: format
format: venv
	$(VENV)/black src tests --exclude=.tox,.venv

include Makefile.venv
