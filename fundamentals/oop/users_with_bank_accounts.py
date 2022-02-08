
class User:
    bank_name = "First National Dojo"
    def __init__(self, n, ea):
        self.name = n
        self.email_address = ea
        self.account = BankAccount(0.02, 0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
    def transfer_money(self, other_user, amount):
        if self.account.account_balance - amount < 0:
            print("Transaction decline: insufficient funds")
        else:
            self.account.withdraw(amount)
            other_user.account.deposit(amount)
        return self

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
        print("Balance: $", self.account_balance)
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

Michael = User("Michael G. Scott", "MichaelScarn@DunderMifflin.com")
Dwight = User("Dwight K. Schrute", "DwightKSchrute@DunderMifflin.com")
Jim = User("Jim Halpert", "JimHalpert@DunderMifflin.com")

Michael.make_deposit(500).make_deposit(500).make_deposit(500).make_deposit(500).make_withdrawal(200).display_user_balance()
Dwight.make_deposit(250).make_deposit(250).make_deposit(250).make_deposit(250).make_withdrawal(20).display_user_balance()
Jim.make_deposit(1000).make_deposit(1000).make_withdrawal(100).display_user_balance()

Michael.transfer_money(Jim, 100).display_user_balance()
Jim.display_user_balance()