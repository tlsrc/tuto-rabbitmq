# RabbitMQ sandbox

Following https://www.rabbitmq.com/getstarted.html

## Running 

### Install deps

> brew install docker
> brew install python3
> pip3 install pika

### Run rabbitmq

Using docker
> ./run-rabbit.sh 

### Running examples

Go to the corresponding subfolder and run the python scripts using python3.

## AMQP Concepts

### Overview

Publisher -> Exchange -> Queue -> Consumer

- Publishers publish messages to exchanges
- Exchanges route message copies to queues based on rules (also called bindings)
- Either
    - The broker deliver messages from the queues to their subscribers
    - Consumers pull messages from the queue on demand

Queues, exchanges and bindings are referred to AMQP entities.

### Exchange types

1. Direct exchange : delivers messages to bounded queues if the routing key from the message matches the one from the queue. The default exchange is direct and automatically creates the corresponding queue (useful for simple cases)
2. Fanout exchange : delivers messages to all queues that are bound to it (useful for broadcasting)
3. Topic exchange : delivers messages to one or many queues based on matching the message routing key and the queue routing pattern (useful for targeted pub/sub)
4. Headers exchange : delivers messages based on messages headers and queue binding headers (for more advanced use cases that cannot rely only on a routing key)

Exchanges also have properties
- Name
- Durable or transient (survive a rabbitmq restart or not)
- Auto-delete (deleted when all queues are unbounded to it)
- Arguments (special features)

### Queues

Queues are just ordered collections of messages to be consumed.

They have properties, some of which are the same as exchanges
- Name
- Durable or transient (survive a rabbitmq restart or not)
- Exclusive (used by only one consumer and will be deleted if that connection closes)
- Auto-delete (will be deleted if no connection are made)
- Arguments (special features)

### Bindings

These are routing rules from exchanges to queues. There can be 0, 1 or many bindings from one exchange to one queue.

They can have a routing key (for some specific exchanges like direct or topic) which acts like a filter.

Having bindings as an indirection layer between exchanges and queues enables some particular scenarios.

If there are no bindings from an exchange to any queues (i.e. no queues are bound to that exchange), the message is either dropped or returned to the publisher (depending on the message attributes)