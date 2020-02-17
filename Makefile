.PHONY: tests

tests:
	pip install -e .
	pip install pytest pytest-cov
	pytest --cov=spotify_dl tests/
