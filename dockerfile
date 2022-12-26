FROM python:3.9-slim

RUN apt-get update

RUN apt-get install libpq-dev -y

EXPOSE 8081

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

WORKDIR /app

COPY entrypoint.sh /app

COPY app/ /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
# During debugging, this entry point will be overridden.
CMD ["sh", "entrypoint.sh"]

