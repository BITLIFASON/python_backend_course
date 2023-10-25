import uvicorn
import pika
import json
from fastapi import FastAPI
from models import Order

app = FastAPI(
    title="Homework 4",
    description="Homework for the ITMO course Python Backend",
    contact={"name": "BITLIFASON", "url": "https://github.com/BITLIFASON"},
    version="0.0.4",
    docs_url="/docs",
)

# rmq_url_connection_str = "amqp://guest:guest@localhost:5672/"
# rmq_parameters = pika.URLParameters(rmq_url_connection_str)
# rmq_connection = pika.BlockingConnection(rmq_parameters)
credentials = pika.PlainCredentials("guest", "guest")
rmq_connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="localhost", credentials=credentials, heartbeat=0, port=5672
    )
)
# rmq_properties = pika.BasicProperties(content_type='application/json', content_encoding='UTF-8')
rmq_channel = rmq_connection.channel()

balance = 1000


@app.get("/balance/")
def check_balance():
    global balance
    return {"balance": balance}


@app.put("/balance/")
def change_balance(data: dict):
    global balance
    balance += data["diff"]
    return {"message": "Balance successfully changed."}


@app.post("/order/")
def add_order(order: Order):
    rmq_channel.basic_publish(
        exchange="main_exchange",
        routing_key=order.order_type,
        body=bytes(
            json.dumps({"item_name": order.item_name, "item_price": order.item_price}),
            "UTF-8",
        ),
        # properties=rmq_properties
    )
    return {"message": "Order Received! Thank you for your patience."}


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 80
    uvicorn.run(app, host=host, port=port)
    if KeyboardInterrupt:
        rmq_connection.close()
