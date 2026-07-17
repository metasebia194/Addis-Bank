from abc import ABC, abstractmethod
class BankConfig:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance.bank_name = "Abyssinia Bank"
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 2000

        return cls._instance


class Account(ABC):

    def __init__(self, owner, number, phone, branch, account_type, balance=0):

        self.owner = owner
        self.account_number = number
        self.phone = phone
        self.branch = branch
        self.account_type = account_type
        self.__balance = balance
        self.transactions = []
        self.observers = []
    @property
    def balance(self):
        return self.__balance
    def update_balance(self, amount):
        self.__balance += amount
    def deposit(self, amount):

        self.update_balance(amount)
        self.transactions.append(
            f"Deposit: {amount} ETB"
        )

        self.notify(
            f"{self.owner} deposited {amount} ETB"
        )
    def subscribe(self, observer):

        self.observers.append(observer)
    def notify(self, message):

        for observer in self.observers:
            observer.update(message)
    @abstractmethod
    def withdraw(self, amount):
        pass
    @abstractmethod
    def statement(self):
        pass
class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount > self.balance - 50:
            print("Minimum balance rule violated")
            return
        self.update_balance(-amount)
        self.transactions.append(
            f"Withdraw: {amount} ETB"
        )
        self.notify(
            f"{self.owner} withdrew {amount} ETB"
        )

    def statement(self):
        print("\nSavings Account")
        print("Owner:", self.owner)
        print("Balance:", self.balance)

class CurrentAccount(Account):


    def withdraw(self, amount):

        config = BankConfig()


        if amount > self.balance + config.overdraft_limit:

            print("Overdraft exceeded")
            return


        self.update_balance(-amount)


        self.transactions.append(
            f"Withdraw: {amount} ETB"
        )


        self.notify(
            f"{self.owner} withdrew {amount} ETB"
        )



    def statement(self):

        print("\nCurrent Account")
        print("Owner:", self.owner)
        print("Balance:", self.balance)

class SMSAlert:

    def update(self,message):

        print("[SMS]", message)
class AuditLog:

    def update(self,message):

        print("[LOG]", message)

class AccountFactory:


    @staticmethod
    def create(account_type, owner, number, phone, branch, balance):
        if account_type == "savings":

            return SavingsAccount(
                owner,
                number,
                phone,
                branch,
                balance
            )


        elif account_type == "current":

            return CurrentAccount(
                owner,
                number,
                phone,
                branch,
                balance
            )


acc1 = AccountFactory.create(
    "savings",
    "Amen",
    12345,
    "0911111111",
    "Sarbet",
    5000
)


acc2 = AccountFactory.create(
    "current",
    "Kirubel",
    67890,
    "0922222222",
    "Bole",
    2000
)



sms = SMSAlert()
log = AuditLog()



acc1.subscribe(sms)
acc1.subscribe(log)

acc2.subscribe(sms)
acc2.subscribe(log)



acc1.deposit(500)
acc1.withdraw(1000)


acc2.deposit(1000)
acc2.withdraw(2500)

accounts = [acc1, acc2]


for account in accounts:

    account.statement()