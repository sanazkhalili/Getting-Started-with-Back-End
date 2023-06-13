import pika

directs_queue = ['modify', 'add']

def callback(cha, method, prop, body):
    print( body)

credent = pika.PlainCredentials(username = 'sanaz' ,
                                   password = '111111', erase_on_connect = True )
param = pika.ConnectionParameters(host = '192.168.241.128',
                          port = 5672,
                          virtual_host = 'my_doc',
                          credentials = credent)
conn = pika.BlockingConnection(parameters = param)

channel = conn.channel()
channel.exchange_declare(exchange = "direct_doc", exchange_type = "direct")


res = channel.queue_declare(queue = '', exclusive = True)
name = res.method.queue


for i in directs_queue:
    channel.queue_bind(queue = name, exchange = "direct_doc", routing_key = i)


channel.basic_consume(queue = name,
                      on_message_callback = callback, auto_ack = True)


channel.start_consuming()
