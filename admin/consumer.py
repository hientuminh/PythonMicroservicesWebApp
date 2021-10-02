import pika

params = pika.URLParameters('amqps://cvetjqbd:slwQt5fuCwrrAH0Q-vruWWmGWOWC0vJW@cattle.rmq2.cloudamqp.com/cvetjqbd')

connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
  print('received in admin')
  print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()

channel.close()