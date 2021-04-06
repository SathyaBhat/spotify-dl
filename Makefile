.PHONY: tests clean
default: tests

clean:
	find . | grep -E "\(__pycache__|\.pyc|\.pyo$\)" | xargs rm -rf

tests: clean
	pip install -e .
	pip install pytest pytest-cov
	pytest --cov=spotify_dl tests/
