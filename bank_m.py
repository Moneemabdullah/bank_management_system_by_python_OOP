import random
import datetime
class Account:
    def __init__(self, name, email, account_type):
        self.name = name
        self.email = email
        self.balance = 0
        self.account_type = account_type
        self.account_no = ""
        self.loan_count = 0 
        self.transaction_history = []

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


class Bank:
    def __init__(self, name):
        self.name = name
        self.total_amount = 0
        self.loans = {}
        self.accounts = {}
        self.is_bankrupt = False

    def add_account(self, user):
        bank_initials = (self.name[0] + self.name[1]) if len(self.name) >= 2 else self.name
        user_initials = (user.name[0] + user.name[1]) if len(user.name) >= 2 else user.name
        account_no = f"0{bank_initials.upper()}{user_initials.upper()}000{len(self.accounts) + 1}"

        self.accounts[account_no] = user
        return account_no

    def delete_account(self, account_no):
        if account_no in self.accounts:
            del self.accounts[account_no]
            print(f"Account no: {account_no} has been deleted successfully")
        else:
            print(f"Account no: {account_no} does not exist.")

    def withdraw_money(self, account_no, amount):
        if account_no in self.accounts:
            if self.accounts[account_no].balance >= amount:
                self.accounts[account_no].balance -= amount
                print(f"Withdrew {amount} from account no: {account_no}")
            else:
                print("Withdrawal amount exceeded")
        else:
            print(f"Account no: {account_no} does not exist.")

    def deposit_money(self, account_no, amount):
        if account_no in self.accounts:
            self.accounts[account_no].balance += amount
            print(f"Deposited {amount} to account no: {account_no}")
        else:
            print(f"Account no: {account_no} does not exist.")

    def new_loan(self, account_no, amount):
        if self.is_bankrupt:
            print("Sorry, you can't get a loan")
            return
        elif self.accounts[account_no].loan_count == 2:
            print("Sorry You cant get lone more then two times")
            return
        if account_no in self.accounts:
            self.accounts[account_no].balance += amount
            self.loans[account_no] = self.loans.get(account_no, 0) + amount
            print(f"Loan of {amount} granted to account no: {account_no}")
            self.accounts[account_no].loan_count += 1
        else:
            print(f"Account no: {account_no} does not exist.")

    def control_loan(self):
        print('Do you want to stop providing loans:\n1. Yes\n2. No')
        choice = int(input("Choice: "))
        self.is_bankrupt = (choice == 1)

    def transfer_money(self, owner_account, target_account, amount):
        if owner_account in self.accounts and target_account in self.accounts:
            if self.accounts[owner_account].balance >= amount:
                self.accounts[owner_account].balance -= amount
                self.accounts[target_account].balance += amount
                print(f"Transferred {amount} from account no: {owner_account} to account no: {target_account}")
            else:
                print("Withdrawal amount exceeded")
        else:
            print("One of the accounts does not exist.")

    def check_balance(self, account_no):
        if account_no in self.accounts:
            money = self.accounts[account_no].balance
            print(f'You have total {money}')
        else:
            print(f"Account no: {account_no} does not exist.")

bank = Bank("Sonar Bank")

def user_interface():
    name = input("Enter your name: ")
    user = User(name, bank)
    user.bank = bank 

    while True:
        print(f"======== Welcome {name} ==========")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Take Loan")
        print("6. Transfer Money")
        print("7. Transaction History")
        print("8. Return to Main Menu")

        choice = input("Enter a choice: ")

        if choice == '1':
            email = input("Enter Email: ")
            account_choice = input("This bank offers 2 types of accounts:\n1. Savings\n2. Current\nEnter your account choice: ")
            account_type = 'Savings' if account_choice == '1' else 'Current'
            user.create_account(account_type, email)
        elif choice == '2':
            user.check_balance()
        elif choice == '3':
            amount = float(input('Enter amount of money you want to deposit: '))
            user.deposit_amount(amount)
        elif choice == '4':
            amount = float(input('Enter amount of money you want to withdraw: '))
            user.withdraw_amount(amount)
        elif choice == '5':
            amount = float(input('Enter amount of money you want to loan: '))
            user.take_loan(amount)
        elif choice == '6':
            receiver_ac_no = input("Enter receiver AC no: ")
            amount = float(input('Enter amount of money you want to transfer: '))
            user.transfer_amount(receiver_ac_no, amount)
        elif choice == '7':
            user.view_transaction_history()
        elif choice == '8':
            return
        else:
            print("Invalid input")

def admin_interface():
    name = input("Enter your name: ")
    admin = Admin(name, "admin@example.com", bank)

    while True:
        print(f"======== Welcome {name} ==========")
        print("1. Create Account")
        print("2. Delete an Account")
        print("3. User Account List")
        print("4. Total Available Balance of Bank")
        print("5. Total Loan Amount")
        print("6. Control Loans")
        print("7. Return to Main Menu")

        choice = input("Enter a choice: ")

        if choice == '1':
            user_name = input("Enter the user's name: ")
            admin.create_account(user_name)
        elif choice == '2':
            account_no = input("Enter account number to delete: ")
            admin.delete_account(account_no)
        elif choice == '3':
            admin.all_accounts()
        elif choice == '4':
            admin.total_balance()
        elif choice == '5':
            admin.total_loans()
        elif choice == '6':
            admin.manage_loans()
        elif choice == '7':
            return
        else:
            print("Invalid input")

print('**********WELCOME**********')
while True:
    print('1. User')
    print('2. Admin')
    print('3. Exit')

    choice = input("Enter choice: ")
    if choice == '1':
        user_interface()
    elif choice == '2':
        admin_interface()
    elif choice == '3':
        break
    else:
        print("Invalid input")

print("************ THANK YOU *************")