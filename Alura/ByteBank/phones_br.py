import re

class PhonesBr:
    def __init__(self, phone):
        if self.valid_phone(phone):
            self.number = phone
        else:
            raise ValueError("Número incorreto!!")

    def valid_phone(self, phone):
        standard = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5}[0-9]{4})"
        respost = re.findall(standard, phone)
        if respost:
            return True
        else:
            return False

    def __str__(self):
        return self.format_phone()

    def format_phone(self):
        standard = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        respost = re.search(standard, self.number)
        formatted_phone = "+{}({}){}-{}".format(
            respost.group(1),
            respost.group(2),
            respost.group(3),
            respost.group(4)
        )
        return formatted_phone
