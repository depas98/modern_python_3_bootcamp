class BankAccount:

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


mike_account = BankAccount("mike")
mike_account.deposit(100)
mike_account.withdraw(10)

print(f"{mike_account.owner} balance is {mike_account.get_balance()}")
