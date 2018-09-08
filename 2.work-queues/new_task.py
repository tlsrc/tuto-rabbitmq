#! /usr/bin/env python3

import sys
import pika

connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.queue_declare(queue='work-queue', durable=True)
#make queue persistent, needs to be set for every component connecting to the queue
#queue must be deleted if not created correctly

message = ' '.join(sys.argv[1:]) or 'Hello World!'
channel.basic_publish(exchange='',
                        routing_key='work-queue',
                        body=message,
                        properties=pika.BasicProperties(delivery_mode=2))
#make message persistent  but not 100% safe (sse publisher confirms)

print(' [x] Sent ' + message)