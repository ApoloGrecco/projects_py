from account import Account
from decimal import *

def main():

    account = Account(123, "Apolo", 100.00, 0.00)
    account2 = Account(456, "Nico", 500.00, 0.00)

    account2.withdraw(Decimal(480.00))
    account2.transfer(Decimal(500), account)

if(__name__== "__main__"):
    main()