#! /usr/bin/env python3

import pika

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.queue_declare(queue='hello') #idempotent

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print("     Channel : " + str(ch))
    print("     Method : " + str(method))
    print("     Properties : " + str(properties))

channel.basic_consume(callback, queue='hello', no_ack=True)

print(" [*] Waiting for messages, To exit press CTRL+C")
channel.start_consuming()