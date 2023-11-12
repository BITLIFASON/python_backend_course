import pika
from logic_buy import order_buy
from logic_sell import order_sell


def on_open(connection):
    connection.channel(on_open_callback=on_channel_open)


def on_channel_open(channel):
    channel.basic_consume(queue="buy", on_message_callback=order_buy)
    channel.basic_consume(queue="sell", on_message_callback=order_sell)


rmq_url_connection_str = "amqp://guest:guest@localhost:5672/"
rmq_parameters = pika.URLParameters(rmq_url_connection_str)
rmq_connection = pika.SelectConnection(
    parameters=rmq_parameters, on_open_callback=on_open
)


try:
    rmq_connection.ioloop.start()
except KeyboardInterrupt:
    rmq_connection.close()
