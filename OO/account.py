from decimal import *
from typing import List

class Account:

    def __init__(self, number, holder, balance, limit = 1000.0):
        print("building account...")
        self.__number = number
        self.__holder = holder.title()
        self.__balance = Decimal(balance)
        self.__limit = Decimal(limit)


    def extract(self):
        print(f"Olá Sr(a). {self.__holder}, o saldo da sua conta é de R${self.__balance}\n")

    def deposit(self, value):
        self.__balance += value
       #print(f"Olá Sr(a). {self.get_holder()}, você depositou R${value:.2f} na sua conta\n")

    def withdraw(self, value):
        self.__balance -= value
        #print(f"Olá Sr(a). {self.get_holder()}, você sacou R${value:.2f} da sua conta\n")

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)
        print(f"Olá Sr(a). {self.__holder}, você realizou uma transferencia para {destiny.__holder} no valor de R${value}\n")

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







