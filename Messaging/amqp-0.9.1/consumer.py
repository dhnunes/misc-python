"""

consumer.py - Basic AMQP 0.9.1 Queue consumer

Basic template about how to connect and consume AMQP queues,
using pika library.

This module contains most of explanations about default values.

To add more informations or correct anything, please open a issue.

"""

import pika


credentials = pika.PlainCredentials('username', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters(
            'IP/Hostname of broker', "Port", "Virtual Host", credentials,
            socket_timeout=300))
channel = connection.channel()
"""

Creating a default blocking connection with messaging brokerself,
an oppening a channel.

"""

channel.queue_declare(queue='sample_test', durable=True)

"""

Declaring the queue. In protocol version AMQP 0.9.1
is always a good practice to declare the queue in
consumer and publisher.

"""

def callback(ch, method, properties, body):
    """

    This function is used as a callback action, everytime a new message
    is consumed from queue, this callback method is called.

    """
    print(" [x] Received %r" % body)

channel.basic_consume(callback, queue='sample_test', no_ack=True)
"""

Here is the calling for consume the queue. After the call
this function will block the execution of code and will wait for


"""


channel.start_consuming()
"""
Here our code get in a loop. Our consumer will connect to broker trough
the channel we open using connection object and will call the callback function
we had declared earlier and will execute the provided actionself.
Mainly, it will only exit in a interruption or an error.

"""
