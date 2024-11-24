FROM python:3.12 AS builder

WORKDIR /app/

RUN apt update  \
    && apt install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*
    
RUN --mount=type=bind,source=requirements.txt,target=/app/requirements.txt \
  pip wheel --no-cache-dir --no-deps -r /app/requirements.txt --wheel-dir /app/wheels

RUN --mount=type=bind,source=requirements.txt,target=/app/requirements.dev.txt \
  pip wheel --no-cache-dir --no-deps -r /app/requirements.dev.txt --wheel-dir /app/wheels


#2#
FROM python:3.12-slim

COPY --from=builder /app/wheels /wheels

RUN pip install --upgrade pip && pip install --no-cache --no-cache-dir /wheels/*

WORKDIR /app
COPY . .

CMD ["python", "backend.py"]
