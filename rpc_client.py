import sys, pika, json, os
from datetime import datetime

class RpcClient(object):
        def __init__(self, ip_addr, uname):
                self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=ip_addr,
                        virtual_host="final_team_8", credentials=pika.PlainCredentials("team_8_user", "atm", True)))
                self.name = uname
                self.channel = self.connection.channel()

                result = self.channel.queue_declare(exclusive=True)
                self.callback_queue = result.method.queue

                self.channel.basic_consume(self.on_response, no_ack=True, queue=self.callback_queue)

        def on_response(self, ch, method, props, body):
                print body
                if "picture_data" in body:
                        tmp = json.loads(body)
                        name = tmp['picture_data']
                        # if not name=="":
                        #         os.system("scp pi@172.30.60.112:~/ECE4564/final/clients/"+self.name+"/" + name + " .")
                self.channel.stop_consuming()

        def call(self, msg, key):
                self.channel.basic_publish(exchange='', routing_key=key,
                        properties=pika.BasicProperties(reply_to=self.callback_queue), body = msg)
                self.channel.start_consuming()
