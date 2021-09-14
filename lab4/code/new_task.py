import pika
import sys

dirIP = "54.152.119.37"
portID = 5672

connection = pika.BlockingConnection(pika.ConnectionParameters(dirIP, portID, "/", pika.PlainCredentials("user","password")))
channel = connection.channel()

channel.queue_declare(queue='my_app', durable=True) #new queue "task_queue" created

message = ' '.join(sys.argv[1:]) or "Hello World!" #message resolved from commandline, if no message then "Hello World!" sent
channel.basic_publish(exchange='', #default exchange
                      routing_key='my_app',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print (" [x] Sent %r" % (message,))
connection.close()