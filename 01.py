import re
from functools import wraps


def email_parse(email_address: str):
    email_parser = re.compile('^(.+)@(.+\.[a-z]{2,})')
    if not email_parser.match(email_address):
        raise ValueError

    passed_email = email_parser.findall(email_address)
    return {'username': passed_email[0][0], 'domain': passed_email[0][1]}


print(email_parse('someone@geekbrains.ru'))
