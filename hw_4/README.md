# Simple personal budget tracker

Idea: orders coming to the service are recorded in the broker, and then processed by celery workers, who change the balance.

The service is available at http://localhost:80/ .

Endpoints (method, router, destination, input data):

- GET - /balance/ - get balance
- PUT - /balance/ - change balance - json with "diff" value
- POST - /order/ - add order - json with "order_type" (buy, sell), "item_name", "item_price" values

Run instruction:
```python

# run container with RabbitMQ
docker run -d --rm --name my-rabbit -p 5672:5672 -p 15672:15672 rabbitmq:3-management

# install library
pip install --no-cache-dir -r requirements.txt

# after start RabbitMQ (15 seconds) run configuration
python configuration.py

# run producer
python producer.py

# run celery worker for sell operation
celery -A logic_sell worker -n sell -Q sell

# run celery worker for buy operation
celery -A logic_buy worker -n buy -Q buy

# run asynchronous consumer
python consumer_io.py
# or synchronous consumer
python consumer.py

```