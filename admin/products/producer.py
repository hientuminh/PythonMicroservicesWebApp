# amqps://cvetjqbd:slwQt5fuCwrrAH0Q-vruWWmGWOWC0vJW@cattle.rmq2.cloudamqp.com/cvetjqbd
import pika, json

params = pika.URLParameters('amqps://cvetjqbd:slwQt5fuCwrrAH0Q-vruWWmGWOWC0vJW@cattle.rmq2.cloudamqp.com/cvetjqbd')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
  properties = pika.BasicProperties(method)
  channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
