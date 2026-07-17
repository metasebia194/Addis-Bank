class Account:

    def __init__(self, owner, number, phone, 
                 branch, account_type, balance=0):
        self.owner = owner
        self.account_number = number
        self.phone = phone
        self.branch = branch
        self.account_type = account_type
        self.__balance = balance
        self.bank = "Abyssinia bank"
        self.status = "Active"

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.__balance:
            print("Insufficient balance.")
            return
        self.__balance -= amount

    def statement(self):
        print(f"Bank: {self.bank}")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Phone: {self.phone}")
        print(f"Branch: {self.branch}")
        print(f"Account Type: {self.account_type}")
        print(f"Status: {self.status}")
        print(f"Balance: {self.balance} ETB")
        print("-" * 40)


acc = Account(
    "Amen",
    "1234567890",
    "+251987654321",
    "sarbet",
    "Current",
    10000
)

# Transactions
acc.deposit(5000)

acc.statement()