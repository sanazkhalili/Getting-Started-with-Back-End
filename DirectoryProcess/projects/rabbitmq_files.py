import os
import time
import glob
import pika


directs_queue = ['modify', 'add']

credential = pika.PlainCredentials(username = 'sanaz' ,
                                   password = '111111', erase_on_connect = True)
connect_parameter = pika.ConnectionParameters(host = '192.168.241.128',
                          port = 5672,
                          virtual_host = 'my_doc',
                          credentials = credential)

conn = pika.BlockingConnection(parameters = connect_parameter)
channel = conn.channel()
channel.exchange_declare(exchange ="direct_doc" , exchange_type = "direct")


path = "/home/sanaz/IDP/directories/direct1/*"

list_files = glob.glob(path)
print(list_files)
for file in list_files:

    ti_c = os.path.getctime(file)
    ti_m = os.path.getmtime(file)
    c_ti = time.ctime(ti_c)
    m_ti = time.ctime(ti_m)
    channel.basic_publish(exchange ="direct_doc" ,
                          routing_key = directs_queue[0],
                          body = str(m_ti)+file)
    channel.basic_publish ( exchange = "direct_doc",
                            routing_key = directs_queue[1],
                            body = str(c_ti ) + file )
    
conn.close()




