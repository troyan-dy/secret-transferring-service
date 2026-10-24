setup:
	pip3 install -r requirements.txt
	pip3 install -r resuirements.dev.txt
test:
	python3 -m pytest tests/

lint:
	python3 -m mypy secret_transferring_service/
	python3 -m flake8 secret_transferring_service/ tests/

wps:
	python3 -m flake8 secret_transferring_service/ tests/ --select=WPS

format:
	python3 -m black secret_transferring_service/ tests/
	python3 -m isort secret_transferring_service/ tests/

start:
	docker-compose up -d --build  && docker-compose logs -f
stop:
	docker-compose down
