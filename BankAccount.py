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

        Args: self, amount(float), account_num(str)

        Return: None
        """

        account_index = find_account(account_num)
        self.accounts[account_index].deposit(amount)

    def find_account(self, account_num):
        """
        finds an account held in the bank via the bank account number

        Args: self, account_num(int)
        """

        for i in range(len(self.accounts)):
            if account.get_account_number() == account_num:
                return i
        print("Unable to find account with matching account number")
        return None

class BankAccount:
    """
    A python class to approximate how a bank account works
    """

    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance

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

        Return: None
        """

        if self.balance - amount > 0:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount} new balance: ${self.balance}")

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

        Args: self, account_number(str)

        return: (str)
        """

        length = len(self.account_number)
        last4 = self.account_number[-4:length]

        return "*" * (length-4) + last4

# testing

account1 = BankAccount("Bob Cheddar", "00123456", 10000)
account2 = BankAccount("Alfalfa Smith", "00069420", 170)
account3 = BankAccount("Andreas Three", "000333333", 300000000000)

bank1 = Bank(account1, account2, account3)

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

bank1.deposit(300, "03141592")