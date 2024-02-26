#!/usr/bin/env python
import pika
from generatePass import generate_pass

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

message = generate_pass()

channel.basic_publish(exchange='', routing_key='hello', body=message)
print(f" [x] Sent password!")
connection.close()
