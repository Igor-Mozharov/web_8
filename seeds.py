import json

from connect import Author, Quotes


def create_authors():
    with open('authors.json', 'r') as file:
        res = json.load(file)
        for author in res:
            base = Author(fullname=author['fullname'], born_date=author['born_date'], born_location=author['born_location']\
                            , description=author['description']).save()
#

def create_quotes():
    with open('quotes.json', 'r') as quote_file:
        res_quote = json.load(quote_file)
    for autor_object in Author.objects():
        for quott in res_quote:
            if autor_object.fullname == quott['author']:
                result = Quotes(tags=quott['tags'], author=autor_object, quote=quott['quote']).save()

if __name__ == '__main__':
    create_authors()
    create_quotes()
