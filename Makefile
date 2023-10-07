build:
	pipenv run python documentation.py

dependencies:
	mkdir .venv
	pipenv install --dev

clean:
	rm -fr output
	rm -fr .venv
	rm Pipfile.lock
