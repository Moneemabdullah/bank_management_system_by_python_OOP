import random
class Account:
    def __init__(self, name, email, account_type):
        self.name = name
        self.email = email
        self.balance = 0
        self.account_type = account_type
        self.account_no = ""
        self.loan_count = 0 
        self.transaction_history = []

