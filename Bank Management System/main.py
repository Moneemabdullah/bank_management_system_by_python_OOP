from bank import Bank
from people import User, Admin

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