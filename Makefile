test:
	pytest -v --cov=vinterunofficial --disable-pytest-warnings &&\
		readme-cov

testhtml:
	pytest -v --cov=vinterunofficial --cov-report=html --disable-pytest-warnings &&\
		readme-cov

install:
	pip install --upgrade pip &&\
		python -m pip install -r requirements.txt

doc:
	cd docs && make html

pre-commit-file:
    pre-commit install
