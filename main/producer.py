import pika, json

params = pika.URLParameters('amqps://mholkzlf:zlfcnGFMArtcz9nk34Xi2ZNBaEtm3tHZ@cow.rmq2.cloudamqp.com/mholkzlf')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
