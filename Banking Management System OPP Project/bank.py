
class Bank:
    def __init__(self, name):
        self.name = name
        self.total_balance = 0
        self.users = []
        self.admins = []
        self.loan_feature = True
        self.total_loan = 0

    def create_bank_account(self, user_info):
        self.users.append(user_info)
        user_info.bank = self

    def create_admin_account(self, admin_info):
        self.admins.append(admin_info)
        admin_info.bank = self
   