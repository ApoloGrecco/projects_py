from decimal import *

class Account:

    def __init__(self, number, holder, balance, limit = 1000.0):
        print("building account...")
        self.__number = number
        self.__holder = holder
        self.__balance = Decimal(balance)
        self.__limit = Decimal(limit)

    def extract(self):
        print(f"Olá Sr(a). {self.__holder}, o saldo da sua conta é de R${self.__balance}\n")

    def deposit(self, value):
        self.__balance += value
        print(f"Olá Sr(a). {self.__holder}, você depositou R${value:.2f} na sua conta")
        self.extract()

    def withdraw(self, value):
        self.__balance -= value
        print(f"Olá Sr(a). {self.__holder}, você sacou R${value:.2f} da sua conta")
        self.extract()

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)






