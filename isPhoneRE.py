# isPhoneRE
# Caleb Bell
# Improved version of isPhone but with Regular Expressions

import re


def is_phone(phone_number):
    phone_numregex = re.compile(r'\d{3}-\d{3}-\d{4}')
    phone_search = phone_numregex.search(phone_number)

    if phone_search is None:
        statement = phone_number + " WAS NOT FOUND!"
    else:
        statement = phone_number + " WAS FOUND!"

    return statement


print(is_phone('This ain\'t no phone number'))
print(is_phone('968-543-1234'))
