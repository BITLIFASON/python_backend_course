FROM python:3.10-slim-buster 

WORKDIR /app

COPY ./requirements_addition.txt ./requirements_addition.txt

RUN pip install --no-cache-dir -r requirements_addition.txt

COPY sentiment_serivce .

EXPOSE 8002

ENTRYPOINT ["python", "main.py"]