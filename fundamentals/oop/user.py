
class User:
    bank_name = "First National Dojo"
    def __init__(self, n, ea):
        self.name = n
        self.email_address = ea
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        if self.account_balance - amount < 0:
            print("Transaction decline: insufficient funds")
        else:
            self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.name + " Account Balance: $" + str(self.account_balance))
        if self.account_balance == 0:
            print("Get your bread up, " + self.name)
    def transfer_money(self, other_user, amount):
        if self.account_balance - amount < 0:
            print("Transaction decline: insufficient funds")
        else:
            self.account_balance -= amount
            other_user.account_balance += amount
        return self

Michael = User("Michael G. Scott", "MichaelScarn@DunderMifflin.com")
Dwight = User("Dwight K. Schrute", "DwightKSchrute@DunderMifflin.com")
Jim = User("Jim Halpert", "JimHalpert@DunderMifflin.com")

Michael.make_deposit(1000).make_deposit(1000).make_deposit(1000).make_withdrawal(2500).display_user_balance()
print()

Dwight.make_deposit(700).make_deposit(700).make_withdrawal(3).make_withdrawal(7).display_user_balance()
print()

Jim.make_deposit(700).make_withdrawal(15).make_withdrawal(10).make_withdrawal(25).display_user_balance()
print()

Michael.transfer_money(Jim, 50)
Michael.display_user_balance()
Jim.display_user_balance()