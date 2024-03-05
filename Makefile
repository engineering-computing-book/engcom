.PHONY: pypi conda

pypi:
	poetry lock
	poetry build
	poetry publish

conda: environment.yaml

environment.yaml:
	conda env export | grep -v "^prefix: " > environment.yml