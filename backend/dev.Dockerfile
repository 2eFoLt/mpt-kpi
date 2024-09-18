FROM python:3.12
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

COPY requirements.txt .
COPY requirements.dev.txt .

RUN python -m pip install --upgrade pip && \
    pip install pip-tools && \
    pip install -r requirements.txt && \
    pip install -r requirements.dev.txt

COPY . .

CMD ["python", "main.py"]
