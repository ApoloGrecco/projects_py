from account import Account
from decimal import *

def main():

    account = Account(123, "apolo", 100.00, 1000.00)
    account2 = Account(456, "nico", 500.00, 1000.00)

    account2.transfer(Decimal(500.00), account)

    account.extract()

if(__name__== "__main__"):
    main()