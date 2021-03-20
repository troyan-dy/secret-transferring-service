setup:
	pip3.9 install -r requirements.txt
	pip3.9 install -r resuirements.dev.txt
test:
	python3.9 -m pytest tests/

lint:
	python3.9 -m mypy fastapi_app/
	python3.9 -m flake8 fastapi_app/ tests/

format:
	python3.9 -m black fastapi_app/ tests/
	python3.9 -m isort fastapi_app/ tests/

start:
	docker-compose up -d --build  && docker-compose logs -f
stop:
	docker-compose down
