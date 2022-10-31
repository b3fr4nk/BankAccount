import random

class Bank:
    """
    A python class to hold bank accounts in a central location

    Args: list of BankAccount objects

    Return: Bank object
    """

    accounts = []

    def __init__(self, *accounts):
        for account in accounts:
            self.accounts.append(account)

    def create_account(self, account):
        """
        Adds a new account to the bank

        Args: self, BankAccount object

        Return: None
        """

        self.accounts.append(account)

    def deposit(self, amount, account_num):
        """
        deposits money into account with specified account number

        Args: self, amount(float), account_num(int)

        Return: None
        """

        account_index = self.find_account(account_num)
        self.accounts[account_index].deposit(amount)

    def withdraw(self, amount, account_num):
        """
        withdraws money into account with specified account number

        Args: self, amount(float), account_num(int)

        Return: None
        """

        account_index = self.find_account(account_num)
        self.accounts[account_index].withdraw(amount)

    def transfer(self, amount, to_account_num, from_account_num):
        """
        moves an amount of money from one accoun to another

        Args: self, amount, to_account_num(int), from_account_num(int)

        Return: bool
        """

        to_account_index = self.find_account(to_account_num)
        from_account_index = self.find_account(from_account_num)

        #check if from account has enough money available
        withdrawn = self.accounts[from_account_index].withdraw(amount)
        if withdrawn:
            self.accounts[to_account_index].deposit(amount)
            print("transfer complete")
            return True
        return False



    def withdraw(self, amount, account_num):
        """
        withdraws money into account with specified account number

        Args: self, amount(float), account_num(int)

        Return: None
        """

        account_index = self.find_account(account_num)
        self.accounts[account_index].withdraw(amount)

    def transfer(self, amount, to_account_num, from_account_num):
        """
        moves an amount of money from one accoun to another

        Args: self, amount, to_account_num(int), from_account_num(int)

        Return: bool
        """

        to_account_index = self.find_account(to_account_num)
        from_account_index = self.find_account(from_account_num)

        withdrawn = self.accounts[from_account_index].withdraw(amount)
        if withdrawn:
            self.accounts[to_account_index].deposit(amount)
            print("transfer complete")
            return True
        return False



    def find_account(self, account_num):
        """
        finds an account held in the bank via the bank account number

        Args: self, account_num(int)
        """
        #loop over every account in bank to find the account with a matching account number
        for i in range(len(self.accounts)):
            print(i)
            if self.accounts[i].account_number == account_num:
                return i
        print("Unable to find account with matching account number")
        return None

class BankAccount:
    """
    A python class to approximate how a bank account works
    """

    balance = 0
    account_number = random.randrange(10000000, 99999999)

    def __init__(self, full_name):
        self.full_name = full_name


    def deposit(self, amount):
        """
        Adds an amount to the current balance of the bank account

        Args: self amount(int)

        Return: None
        """

        self.balance += amount
        print(f"Amount deposited: ${amount} new balance: ${self.balance}")

    def withdraw(self, amount):
        """
        Removes an amount from the current balance of the bank account

        Args: self, amount(int)

        Return: bool
        """

        if self.balance - amount > 0:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount} new balance: ${self.balance}")
            return True
        print("insuficient funds")
        return False

    def get_balance(self):
        """
        Adds an amount to the current balance of the bank account

        Args: self

        Return: current balance of the bank account
        """

        print(f"You currently have ${self.balance} in your account")
        return self.balance

    def add_interest(self):
        """
        Adds a pre-determined interest rate to the current balance of the account on a monthly basis

        Args: self

        Return: None
        """

        interest = self.balance * 0.00083
        self.balance += interest

    def print_statement(self):
        """
        prints a user friendly bank statement to the console that includes full name, the last four digits of the account number, and their balance

        Args: self

        Return: none
        """

        hidden_num = self.hide_account_number(self.account_number)
        print(f"{self.full_name}\nAccount No.: {hidden_num}\nBalance:{self.balance}")

    def hide_account_number(self, account_number):
        """
        hides all but the last four digits of the account number

        Args: self, account_number(int)

        return: (str)
        """
        account_num_str = f"{self.account_number}"
        length = len(account_num_str)
        last4 = account_num_str[-4:length]

        return "*" * (length-4) + last4

# testing

account1 = BankAccount("Bob Cheddar")
account2 = BankAccount("Alfalfa Smith")
account3 = BankAccount("Andreas Three")

bank1 = Bank(account1, account2, account3)

account1.print_statement()

account2.print_statement()
account2.get_balance()

account2.deposit(550)

account2.withdraw(999)

account2.withdraw(450)

account3.deposit(1000000000)
account3.add_interest()
account3.print_statement()

mitchell_account = BankAccount("Mitchell")
bank1.create_account(mitchell_account)

mitchell_account.deposit(400000)

mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.print_statement()

mitchell_account.withdraw(150)
mitchell_account.print_statement()

bank1.deposit(300, mitchell_account.account_number)

bank1.transfer(100, mitchell_account.account_number, account2.account_number)