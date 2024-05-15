FROM python:3.10

WORKDIR /app

COPY models /app/models
COPY routes /app/routes
COPY schema /app/schema
COPY config /app/config
COPY requirements.txt /app
COPY main.py /app

ENV PYTHONPATH=/app

RUN python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--no-server-header", "--no-access-log"]