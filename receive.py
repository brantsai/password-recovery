#!/usr/bin/env python
import pika


def receive(callback):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def on_message_callback(ch, method, properties, body):
        print(f" [x] Your new password is {body}")
        callback(ch, method, properties, body)  # Call the provided callback function
        channel.stop_consuming()

    channel.basic_consume(queue='hello', on_message_callback=on_message_callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        connection.close()

