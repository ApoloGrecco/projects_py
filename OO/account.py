

class Account:

    def __init__(self, number, tittle, balance, limit = 1000.0):
        print("building account...")
        self.number = number
        self.tittle = tittle
        self.balance = balance
        self.limit = limit
