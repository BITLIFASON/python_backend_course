import os
import json
import requests
from celery import Celery

os.environ.setdefault("FORKED_BY_MULTIPROCESSING", "1")

celery = Celery("buy_celery", broker="amqp://guest:guest@localhost:5672/")

celery.conf.task_protocol = 1
celery.conf.update()


def order_buy(channel, method_frame, header_frame, body):
    order = json.loads(body)
    if "item_name" in order.keys():
        order_buy_task.delay(order["item_name"], order["item_price"])
    else:
        order_buy_task.delay(order["args"][0], order["args"][1])
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    return {"message": "Task Complete!"}


@celery.task(name="buy_task", queue="buy")
def order_buy_task(item_name, item_price):
    requests.put(url="http://localhost:80/balance/", json={"diff": -item_price})
    print(f"Buy {item_name} for {item_price} $")
