.PHONY: venv
venv:
	python3 -m venv venv

.PHONY: freeze
freeze:
	pip freeze > requirements.txt

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: run
run:
	ipython -i quiz.py

.PHONY: clean
clean:
	rm quiz.db || true

.PHONY: dev
dev: clean run
