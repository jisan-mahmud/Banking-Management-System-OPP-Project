from person import User, Admin
from bank import Bank
def main():
    bank = Bank('City Bank')

    admin = Admin('Jisan', 'jisan@gmail.com', 'jisan11')
    bank.create_admin_account(admin)

    user1 = User('sun', 'sunbd242@gmail.com', 'sunbd22')
    bank.create_bank_account(user1)
    user2 = User('Mahmud', 'mahmud@gmail.com', 'mahmud2233')
    bank.create_bank_account(user2)

    user1.deposit(1000)

    user1.transfer(user2, 500)
    user2.get_loan(900)

    user2.deposit(10000)
    user1.withdraw(200)
    admin.disable_loan_feature()
    user1.get_loan(500)


    admin.enable_loan_feature()
    user1.get_loan(300)

    print(user1.get_transaction_history())
    print(user2.get_transaction_history())

    print(admin.total_loan_amount())

    print(admin.bank_balance())

    print(user2.check_balance())

if __name__ == '__main__':
    main()