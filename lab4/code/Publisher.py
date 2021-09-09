import pika

dirIP = "54.152.119.37"
portIP = 5672

connection = pika.BlockingConnection(pika.ConnectionParameters(dirIP, portIP, '/', pika.PlainCredentials('user', 'password')))
channel = connection.channel()
channel.basic_publish(exchange='my_exchange', routing_key='test', body='Test!')

print("Runnning Producer Application...")
print(" [x] Sent 'Hello World...!'")

connection.close() 