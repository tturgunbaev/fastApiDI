FROM python:3.11.3
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev gcc netcat-openbsd

RUN mkdir /app -p && mkdir /app/static -p
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app/
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
