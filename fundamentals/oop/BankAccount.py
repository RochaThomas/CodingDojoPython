
from mimetypes import init
from unittest import result


class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate, balance = 0):
        self.interest_rate = int_rate
        self.account_balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.account_balance, amount):
            self.account_balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.account_balance -= 5
        return self
    def display_account_info(self):
        print("Balance:", self.account_balance)
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += (self.account_balance * self.interest_rate)
        return self
    
    @staticmethod
    def can_withdraw(balance, amount):
        result = False
        if balance - amount >= 0:
            result = True
        return result

    @classmethod
    def all_accounts_info(cls):
        for account in cls.all_accounts:
            print(f"Balance: {account.account_balance} Interest Rate: {account.interest_rate * 100}%")

ba1 = BankAccount(0.01)
ba2 = BankAccount(0.02)

ba1.deposit(500).deposit(500).deposit(500).withdraw(200).yield_interest().display_account_info()
# ba2.deposit(2000).deposit(2000).withdraw(1000).withdraw(1000).withdraw(1000).withdraw(1001).yield_interest().display_account_info()
ba2.deposit(2000).deposit(2000).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()

BankAccount.all_accounts_info()