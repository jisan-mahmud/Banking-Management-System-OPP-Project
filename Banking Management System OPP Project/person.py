from bank import Bank
class Person:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password

class User(Person):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)
        self.__balance = 0
        self.__transaction_history = []
        self.__bank = None

    @property
    def bank(self):
        return self.__bank
    @bank.setter
    def bank(self, value):
        self.__bank = value

    def deposit(self, amount):
        if amount > 0 and self in self.__bank.users:
            self.__balance += amount
            self.__bank.total_balance += amount
            self.__transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self in self.__bank.users:
            if self.__bank.total_balance < amount:
                print('The bank is bankrupt')
                return
        
            if self.__balance >= amount:
                self.__bank.total_balance -= amount
                self.__balance -= amount
                self.__transaction_history.append(f"Withdrawn: {amount}")
            else:
                print("Insufficient balance")
        else:
            print('This User Found In This Bank')

    def transfer(self, recipient, amount):
        if self.__balance >= amount and self in self.__bank.users and recipient in self.__bank.users and self.__bank.name == recipient.__bank.name:
            if self.__balance >= amount:
                self.__balance -= amount
                recipient.__balance += amount
                self.__transaction_history.append(f"Transferred: {amount} to {recipient.email}")
                recipient.__transaction_history.append(f"Received: {amount} from {self.email}")
            else:
                print("Insufficient balance")
    
    def get_loan(self, amount):
        if self in self.__bank.users:
            if (self.__balance * 2) >= amount  and self.__bank.total_balance >= amount and self.bank.loan_feature == True:
                self.__balance += amount
                self.__bank.total_balance -= amount
                self.__bank.total_loan += amount
                self.__transaction_history.append(f"Loan : {amount}")
   
    def check_balance(self):
        if self in self.__bank.users:
            return self.__balance

    def get_transaction_history(self):
        if self in self.__bank.users:
            temp = ''
            temp += f'------Transaction History------\n'
            for value in self.__transaction_history:
                temp += f'{value}\n'
            return temp

class Admin(Person):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)
        self.__bank = None

    @property
    def bank(self):
        return self.__bank
    @bank.setter
    def bank(self, value):
        self.__bank = value

    def bank_balance(self):
        if self in self.__bank.admins:
            return self.__bank.total_balance
        else:
            return 'Admin Not Exits This Bank'
        
    def total_loan_amount(self):
        if self in self.__bank.admins:
            return self.__bank.total_loan
        
    def enable_loan_feature(self):
        if self in self.__bank.admins:
            self.__bank.loan_feature = True
    def disable_loan_feature(self):
        if self in self.__bank.admins:
            self.__bank.loan_feature = False 