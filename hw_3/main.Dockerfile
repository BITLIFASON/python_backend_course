FROM python:3.10-slim-buster 

WORKDIR /app

COPY ./requirements_main.txt ./requirements_main.txt

RUN pip install --no-cache-dir -r requirements_main.txt

COPY main_service .

EXPOSE 8001

ENTRYPOINT ["python", "main.py"]