class BankAccount:

    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount} new balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount} new balance: ${self.balance}")

    def get_balance(self):
        print(f"You currently have ${self.balance} in your account")
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest

    def print_statement(self):
        hidden_num = self.hide_account_number(self.account_number)
        print(f"{self.full_name}\nAccount No.: {hidden_num}\nBalance:{self.balance}")

    def hide_account_number(self, account_number):
        length = len(self.account_number)
        last4 = self.account_number[-4:length]

        return "*" * (length-4) + last4

account1 = BankAccount("Bob Cheddar", "00123456", 10000)
account2 = BankAccount("Alfalfa Smith", "00069420", 170)
account3 = BankAccount("Andreas Three", "000333333", 300000000000)

account1.print_statement()

account2.print_statement()
account2.get_balance()

account2.deposit(350)

account2.withdraw(999)

account2.withdraw(450)

account3.add_interest()
account3.print_statement()

mitchell_account = BankAccount("Mitchell", "03141592", 0)

mitchell_account.deposit(400000)

mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.print_statement()

mitchell_account.withdraw(150)
mitchell_account.print_statement()