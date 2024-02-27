#!/usr/bin/env python
import pika
from generatePass import generate_pass


def send():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    message = generate_pass()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(f" [x] Sent password request!")
    connection.close()
