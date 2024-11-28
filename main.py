class Bank:
    def __init__(self, user_name, initial_amount):
        self.user_name = user_name
        self.balance = initial_amount

    # method to fetch balance declared here
    def get_balance(self):
        return self.balance

    # method to deposit money into account declared here
    def deposit_money(self, amount):
        if amount <= 0:
            print('Deposit Amount Must Be Greater Than Zero!!\n')
            return

        print('Amount Successfully Deposited To Your Account!!\n')
        self.balance += amount

    # method to withdraw money from account declared here
    def withdraw_money(self, amount):
        if amount > self.balance:
            print('Insufficient Balance!!\n')
            return
        elif amount <= 0:
            print('Withdraw Amount Must Be Greater Than Zero!!\n')
            return

        print('Amount Successfully Withdrawn From Your Account!!\n')
        self.balance -= amount

# creating Bank class object here
account = Bank('Milhan Joardar Aumi', 10000)

print('Welcome To Bank Management System!!')
print(f'Bank Account Holder: {account.user_name}')
print(f'Initial Balance: {account.balance}\n')

while True:
    print('0. Exit')
    print('1. Deposit Money')
    print('2. Withdraw Money')
    print('3. Balance Inquiry\n')

    choice = input('Choose An Option: ')

    if choice == '0':
        print('Thank You For Using Bank Management System!!\n')
        break

    elif choice == '1':
        try:
            amount = int(input('Enter The Amount You Want To Deposit: '))

            account.deposit_money(amount)
        except Exception as e:
            print('Given Amount Is Invalid!!\n')

    elif choice == '2':
        try:
            amount = int(input('Enter The Amount You Want To Withdraw: '))

            account.withdraw_money(amount)
        except Exception as e:
            print('Given Amount Is Invalid!!\n')

    elif choice == '3':
        print(f'Your Current Balance: {account.get_balance()}\n')

    else:
        print('Please, Select A Valid Option!!\n')




