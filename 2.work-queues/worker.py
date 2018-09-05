#! /usr/bin/env python3

import time
import pika

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.queue_declare(queue='work-queue', durable=True) #durable=True must be set everywhere

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(' [x] Done')
    ch.basic_ack(delivery_tag = method.delivery_tag)
    # https://www.rabbitmq.com/confirms.html
    # https://www.rabbitmq.com/heartbeats.html

channel.basic_qos(prefetch_count=1) 
# do not give more workers than 1 message at a time
channel.basic_consume(callback, queue='work-queue')

print(" [*] Waiting for messages, To exit press CTRL+C")
channel.start_consuming()