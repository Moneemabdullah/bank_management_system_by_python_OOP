from people import User, Admin

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