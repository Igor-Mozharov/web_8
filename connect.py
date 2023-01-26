import configparser

from mongoengine import connect, Document
from mongoengine.fields import StringField, DateField, ListField, ReferenceField

config = configparser.ConfigParser()
config.read('config.ini')
user_name = config.get('DB', 'user')
password = config.get('DB', 'password')
con = connect(host=f'mongodb+srv://{user_name}:{password}@cluster0.tvqcfdh.mongodb.net/?retryWrites=true&w=majority')


class Author(Document):
    fullname = StringField(required=True)
    born_date = DateField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)


class Quotes(Document):
    tags = ListField(required=True)
    author = ReferenceField(Author)
    quote = StringField(required=True)