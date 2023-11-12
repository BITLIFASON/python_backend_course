import pika


rmq_url_connection_str = f"amqp://guest:guest@localhost:5672/"
rmq_parameters = pika.URLParameters(rmq_url_connection_str)
rmq_connection = pika.BlockingConnection(rmq_parameters)
rmq_channel = rmq_connection.channel()

rmq_channel.queue_declare(queue="buy", durable=True)
rmq_channel.queue_declare(queue="sell", durable=True)

rmq_channel.exchange_declare(exchange="main_exchange", exchange_type="topic")

rmq_channel.queue_bind(exchange="main_exchange", queue="buy", routing_key="buy")
rmq_channel.queue_bind(exchange="main_exchange", queue="sell", routing_key="sell")
