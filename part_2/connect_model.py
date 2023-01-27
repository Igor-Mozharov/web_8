import configparser

from mongoengine import connect, Document, StringField, BooleanField

config = configparser.ConfigParser()
config.read('config.ini')
user_name = config.get('DB', 'user')
password = config.get('DB', 'password')
con = connect(host=f'mongodb+srv://{user_name}:{password}@cluster0.tvqcfdh.mongodb.net/?retryWrites=true&w=majority')


class Contact(Document):
    fullname = StringField(required=True)
    address = StringField(required=True)
    email = StringField(required=True)
    send_message = BooleanField(default=False)
