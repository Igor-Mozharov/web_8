from connect import Author, Quotes


def find_by_name(name):
    quotes = [x.quote for x in Quotes.objects if x.author.fullname == name]
    return quotes


def find_by_tag(tag):
    quotes = [x.quote for x in Quotes.objects if tag in x.tags]
    return quotes


def find_by_tags(tags):
    tags = tags.split(',')
    return [x.quote for x in Quotes.objects(tags__in=tags)]


if __name__ == '__main__':
    while True:
        user_input = input('Yes, Master! What can i do for you?   ')
        user_input = user_input.split()
        match user_input[0]:
            case 'name':
                print(find_by_name(' '.join(user_input[1:])))
            case 'tag':
                print(find_by_tag(' '.join(user_input[1:])))
            case 'tags':
                print(find_by_tags(' '.join(user_input[1:])))
            case 'exit':
                print('Good buy my Master!')
                break
            case _:
                print('Wrong command, my Master, try something else!')