import datetime
from accaount import Account

class User:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.accounts = []
        self.transaction_history = []
        self.account_number = ''

    def create_account(self, account_type, email):
        self.email = email
        self.account_type = account_type
        self.user = Account(self.name, self.email, self.account_type)
        account_no = self.bank.add_account(self.user) 
        self.account_number = account_no 
        print(f"Account created for {self.name} with account number: {account_no}")

    def withdraw_amount(self, amount):
        if self.account_number: 
            self.bank.withdraw_money(self.account_number, amount)
            self.log_transaction("withdrawal", amount)

    def deposit_amount(self, amount):
        if self.account_number:
            self.bank.deposit_money(self.account_number, amount)
            self.log_transaction("deposit", amount)

    def transfer_amount(self, target_account, amount):
        if self.account_number:
            self.bank.transfer_money(self.account_number, target_account, amount)
            self.log_transaction("transfer", amount, target_account)

    def take_loan(self, amount):
        if self.account_number:
            self.bank.new_loan(self.account_number, amount)
            self.log_transaction("loan", amount)

    def log_transaction(self, transaction_type, amount, target_account=None):
        transaction = {
            "type": transaction_type,
            "amount": amount,
            "date": datetime.datetime.now(),
            "target_account": target_account
        }
        self.transaction_history.append(transaction)

    def view_transaction_history(self):
        if not self.transaction_history:
            print("No transaction history available.")
            return
        
        print(f"Transaction History for {self.name}:")
        for transaction in self.transaction_history:
            target_info = f" to account {transaction['target_account']}" if transaction['target_account'] else ""
            print(f"{transaction['date']}: {transaction['type'].capitalize()} of {transaction['amount']}{target_info}")

    def check_balance(self):
        self.bank.check_balance(self.account_number)



class Admin:
    def __init__(self, name, email, bank):
        self.name = name
        self.email = email
        self.bank = bank

    def create_account(self, user_name):
        user = User(user_name)
        account_no = self.bank.add_account(user)
        print(f"Account created for {user_name} with account number: {account_no}")
        return account_no

    def delete_account(self, account_no):
        self.bank.delete_account(account_no)

    def all_accounts(self):
        for account_no, user in self.bank.accounts.items():
            print(f"Account Number: {account_no}, User: {user.name}")

    def total_balance(self):
        total_balance = sum(user.balance for user in self.bank.accounts.values())
        print(f"Total balance of the bank: {total_balance}")

    def total_loans(self):
        total_loans = sum(self.bank.loans.values())
        print(f"Total loan amount: {total_loans}")

    def manage_loans(self):
        self.bank.control_loan()