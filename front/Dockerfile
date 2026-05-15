
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=rainforest.py

WORKDIR /app

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    gdal-bin \
    libgdal-dev \
    curl \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p generated \
  && useradd --create-home appuser \
  && chown -R appuser:appuser /app

USER appuser

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

