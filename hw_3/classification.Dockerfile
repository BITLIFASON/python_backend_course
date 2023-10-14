FROM python:3.10-slim-buster 

WORKDIR /app

COPY ./requirements_addition.txt ./requirements_addition.txt

RUN pip install --no-cache-dir -r requirements_addition.txt

COPY classification_service .

EXPOSE 8003

ENTRYPOINT ["python", "main.py"]