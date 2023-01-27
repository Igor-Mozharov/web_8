import pika
import faker
from connect_model import Contact

credentials = pika.PlainCredentials(username='guest', password='guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare('id_exchange', exchange_type='fanout')
channel.queue_declare(queue='id_queue', durable=True)
channel.queue_bind(exchange='id_exchange', queue='id_queue')


def generate_contacts(number_of_contact: int):
    fake = faker.Faker()
    for _ in range(number_of_contact):
        contact = Contact(fullname=fake.name(), address=fake.address(), email=fake.email()).save()


def send_message():
    for contact in Contact.objects:
        contact.id = str(contact.id)
        channel.basic_publish(exchange='id_exchange', routing_key='id_queue', body=contact.id.encode(), properties=pika.BasicProperties(\
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))
        print(f'[v] sent {contact.id} ')
    connection.close()


if __name__ == '__main__':
    generate_contacts(20)
    send_message()