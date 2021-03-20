FROM python:3.9


COPY requirements.txt requirements.txt

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN pip install --no-cache-dir -r requirements.txt

COPY secret_transferring_service /secret_transferring_service



CMD ["uvicorn", "secret_transferring_service.app:app", "--host=0.0.0.0", "--port=5000"]
