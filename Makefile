test:
	pytest -v --cov=vinterunofficial --disable-pytest-warnings

install:
	pip install --upgrade pip &&\
		python -m pip install -r requirements.txt