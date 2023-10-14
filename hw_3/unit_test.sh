docker build -f sentiment.Dockerfile --tag=sentiment_service .
docker build -f classification.Dockerfile --tag=classification_service .
docker build -f main.Dockerfile --tag=main_service .

# docker run -d -p=8003:8003 --net=service_network --rm --name=classification_service classification_service
# docker run -d -p=8002:8002 --net=service_network --rm --name=sentiment_service sentiment_service
# docker run -d -p=8001:8001 --net=service_network --rm --name=main_service main_service

docker-compose up -d

echo 'Сервисы загружаются...(10 секунд)'
sleep 10
# sleep 120

cd tests && pytest unit_tests.py

# docker stop main_serivce
# docker stop sentiment_serivce
# docker stop classification_serivce

docker-compose down

read -n 1 -s -r -p "Нажмите любую кнопку для завершения"
