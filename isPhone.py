# isPhone
# Caleb Bell
# Provided a string of numbers, determines if the format is correct for phone number


def isPhoneNumber(text):
    """Checks validity of phone number provided"""
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
        if text[3] != '-':
            return False
        for i in range(4, 7):
            if not text[i].isdecimal():
                return False
            if text[7] != '-':
                return False
            for i in range(8, 12):
                if not text[i].isdecimal():
                    return False
                return True

print(isPhoneNumber('2222222222222222222222'))
print(isPhoneNumber('212-345-1254'))