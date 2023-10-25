import pika
from logic_buy import order_buy
from logic_sell import order_sell


rmq_url_connection_str = "amqp://guest:guest@localhost:5672/"
rmq_parameters = pika.URLParameters(rmq_url_connection_str)
rmq_connection = pika.BlockingConnection(rmq_parameters)
rmq_channel = rmq_connection.channel()


rmq_channel.basic_consume(queue="buy", on_message_callback=order_buy)
rmq_channel.basic_consume(queue="sell", on_message_callback=order_sell)


try:
    rmq_channel.start_consuming()
except KeyboardInterrupt:
    rmq_channel.stop_consuming()
    rmq_connection.close()
