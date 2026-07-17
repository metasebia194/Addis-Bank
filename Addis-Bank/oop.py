from abc import ABC, abstractmethod
class Account(ABC):

    def __init__(self, owner, number, phone, branch, account_type, balance=0):
        self.owner = owner
        self.account_number = number
        self.phone = phone
        self.branch = branch
        self.account_type = account_type
        self._balance = balance
        self.bank = "Abyssinia Bank"
        self.status = "Active"

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self._balance += amount
            print(f"Deposited {amount} ETB")
            print(f"New Balance: {self._balance} ETB")

    @abstractmethod
    def withdraw(self, amount):
        pass

    def statement(self):
        print("\n--- Account Statement ---")
        print(f"Bank: {self.bank}")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Status: {self.status}")
        print(f"Balance: {self._balance} ETB")

class SavingsAccount(Account):

    def __init__(self, owner, number, phone, branch, balance=0, interest_rate=0.05):
        super().__init__(
            owner,
            number,
            phone,
            branch,
            "Savings",
            balance
        )

        self.interest_rate = interest_rate
    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal amount")

        elif amount > self._balance - 50:
            print("Savings account must keep minimum 50 ETB")

        else:
            self._balance -= amount
            print(f"Withdrawn {amount} ETB from Savings Account")
    def statement(self):
        super().statement()
        print(f"Interest Rate: {self.interest_rate * 100}%")
        print("------------------------")
class CurrentAccount(Account):

    def __init__(self, owner, number, phone, branch, balance=0, overdraft_limit=2000):

        super().__init__(
            owner,
            number,
            phone,
            branch,
            "Current",
            balance
        )

        self.overdraft_limit = overdraft_limit
    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal amount")

        elif amount > self._balance + self.overdraft_limit:
            print("Overdraft limit exceeded")

        else:
            self._balance -= amount
            print(f"Withdrawn {amount} ETB from Current Account")
    def statement(self):
        super().statement()
        print(f"Overdraft Limit: {self.overdraft_limit} ETB")
        print("------------------------")
accounts = [

    SavingsAccount(
        "Amen",
        "123456",
        "+251987654321",
        "Sarbet",
        1000
    ),

    CurrentAccount(
        "Kirubel",
        "654321",
        "+251911223344",
        "Bole",
        1000
        
    )

]


print("=== Running Transactions ===")


for account in accounts:

    account.deposit(200)

    # Same method call, different behavior
    account.withdraw(1100)

    # Same method call, different output
    account.statement()