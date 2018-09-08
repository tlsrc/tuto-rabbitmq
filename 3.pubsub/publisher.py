#! /usr/bin/env python3

import pika
import sys

connections_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connections_params)

channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or 'Hello World!'
channel.basic_publish(exchange='logs', routing_key='', body=message)

print(" [x] Sent %r" % message)
connection.close()