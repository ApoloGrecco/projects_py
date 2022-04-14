from account import Account
from decimal import *

def main():

    account = Account(123, "apolo", 100.00, 1000.00)
    account.extract()
    account.deposit(Decimal(100.00))
    print(account.balance)

    account2 = Account(321, "Marco", 100.5, 1000.00)
    account2.extract()

    account2.transfer(50, account)

    account = None
    account2 = None

if(__name__== "__main__"):
    main()