# amqps://cvetjqbd:slwQt5fuCwrrAH0Q-vruWWmGWOWC0vJW@cattle.rmq2.cloudamqp.com/cvetjqbd
import pika
import pika

params = pika.URLParameters('amqps://cvetjqbd:slwQt5fuCwrrAH0Q-vruWWmGWOWC0vJW@cattle.rmq2.cloudamqp.com/cvetjqbd')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
  channel.basic_publish(exchange='', routing_key='main', body='hello main')
