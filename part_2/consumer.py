import time

import pika

from connect_model import Contact


credentials = pika.PlainCredentials(username='guest', password='guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='id_queue', durable=True)


def send_email(client_id):
    print('----[send email]')
    client = Contact.objects(id=client_id)
    client.update(send_message=True)

def callback(ch, method, properties, body):
    message = body.decode()
    print(f'[v] received {message}')
    time.sleep(2)
    print(f"[v] Done: {method.delivery_tag}")
    channel.basic_ack(delivery_tag=method.delivery_tag)
    send_email(message)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='id_queue', on_message_callback=callback)


if __name__ == '__main__':
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('Good Luck!')