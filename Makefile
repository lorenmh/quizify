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
	rm quiz.db
