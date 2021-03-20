setup:
	pip3.9 install -r requirements.txt
	pip3.9 install -r resuirements.dev.txt
test:
	python3.9 -m pytest tests/

lint:
	python3.9 -m mypy secret_transferring_service/
	python3.9 -m flake8 secret_transferring_service/ tests/

format:
	python3.9 -m black secret_transferring_service/ tests/
	python3.9 -m isort secret_transferring_service/ tests/

start:
	docker-compose up -d --build  && docker-compose logs -f
stop:
	docker-compose down
