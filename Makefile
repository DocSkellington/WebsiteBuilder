build:
	pipenv run python documentation.py

dependencies:
	mkdir .venv
	pipenv install --dev

release:
	pipenv requirements > requirements.txt
	pipenv run python -m build
	zip release -r \
		requirements.txt dist/ \
		documentation.py sources/ output/ \
		README.md LICENSE

clean:
	rm -fr output

nuke: clean
	rm -fr .venv
	rm Pipfile.lock
