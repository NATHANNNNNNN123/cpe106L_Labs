"""
File: bank.py
This module defines the Bank class.
"""

import pickle
import random
from savingsaccount import SavingsAccount

class Bank:
    """This class represents a bank as a collection of savings accounts."""

    def __init__(self, fileName = None):
        self.accounts = {}
        self.fileName = fileName
        if fileName is not None:
            with open(fileName, 'rb') as fileObj:
                while True:
                    try:
                        account = pickle.load(fileObj)
                        self.add(account)
                    except Exception:
                        break

    def __str__(self):
        """Returns the string representation of the bank, sorted by account name."""
        sorted_accounts = sorted(self.accounts.values())
        return "\n".join(map(str, sorted_accounts))

    def makeKey(self, name, pin):
        return name + "/" + pin

    def add(self, account):
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        total = 0
        for account in self.accounts.values():
            total += account.computeInterest()
        return total

    def getKeys(self):
        return sorted(self.accounts.keys())

    def save(self, fileName = None):
        if fileName:
            self.fileName = fileName
        elif self.fileName is None:
            return
        with open(self.fileName, 'wb') as fileObj:
            for account in self.accounts.values():
                pickle.dump(account, fileObj)

# Functions for testing

def createBank(numAccounts = 1):
    names = ("Brandon", "Molly", "Elena", "Mark", "Tricia",
             "Ken", "Jill", "Jack")
    bank = Bank()
    upperPin = numAccounts + 1000
    for pinNumber in range(1000, upperPin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pinNumber), balance))
    return bank

def testAccount():
    account = SavingsAccount("Ken", "1000", 500.00)
    print(account)
    print(account.deposit(100))
    print("Expect 600:", account.getBalance())
    print(account.deposit(-50))
    print("Expect 600:", account.getBalance())
    print(account.withdraw(100))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(-50))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(100000))
    print("Expect 500:", account.getBalance())

def main(number = 10, fileName = None):
    testAccount()
    bank = createBank(number)
    print(bank)

if __name__ == "__main__":
    main()
