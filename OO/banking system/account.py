from decimal import *


class Account:

    def __init__(self, number, holder, balance, limit=1000.0):
        self.__number = number
        self.__holder = holder.title()
        self.__balance = Decimal(balance)
        self.__limit = Decimal(limit)

    def extract(self):
        print(f"Olá Sr(a). {self.__holder}, o saldo da sua conta é de R${self.__balance}\n")

    def deposit(self, value):
        self.__balance += value
        print(f"Olá Sr(a). {self.__holder}, você depositou R${value:.2f} na sua conta\n")

    def __you_can_withdraw(self, amount_withdraw):
        amount_available_withdraw = self.__balance + self.__limit
        return amount_withdraw <= amount_available_withdraw

    def withdraw(self, value):
        if self.__you_can_withdraw(value):
            self.__balance -= value
            print(f"Olá Sr(a). {self.__holder}, você sacou R${value:.2f} da sua conta\n")
            accomplished = True
        else:
            print(f"Olá Sr(a). {self.__holder}, o valor de R${value} ultrapassou seu limite")
            accomplished = True

    def transfer(self, value, destiny):
        if (accomplished == True):
            self.withdraw(value)
            destiny.deposit(value)
        elif (accomplished == False):
            print("Operação invalida")

    @property
    def balance(self):
        return Decimal(self.__balance)

    @property
    def holder(self):
        return self.__holder

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def bank_codes():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
