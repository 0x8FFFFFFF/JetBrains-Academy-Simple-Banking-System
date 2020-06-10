from random import sample
from datetime import datetime


class Card:
    """Bank card data model"""
    id = 0        # INTEGER
    number = ''   # TEXT
    pin = ''      # TEXT
    balance = 0   # INTEGER DEFAULT 0


class Account(Card):
    """Customer account, upon initialization takes the client id.
    Since, by condition, a client can have only one bank card, then client id = card id."""
    def __init__(self):
        self.id = int(datetime.today().strftime("%d%H%M%S"))*10  # generator of account identifier
        self.number = str(4000000000000000 + self.id)            # generator of number of the card
        self.pin = ''.join(map(str, sample(range(0, 9), 4)))     # generator of random 4 digits pin code


class Banking:
    """Banking system"""
    def __init__(self):
        self.menu_choice = ''
        self.current_account = None
        self.accounts = {}  # temporary dict (database) for accounts

    def menu(self, types='main'):
        """The program menu, shows menu items and processes user input and menu selection"""
        if types == 'main':
            print('1. Create an account')
            print('2. Log into account')
            print('0. Exit')
            self.menu_choice = input()
        elif types == 'account':
            print('1. Balance')
            print('2. Log out')
            print('0. Exit')
            self.menu_choice += '.' + input()  # create submenu

    def create_account(self):
        """Creates a customer account"""
        account = Account()
        self.accounts[account.id] = account  # temporary solution
        # show the result according to the condition of the task
        print('Your card has been created')
        print('Your card number:')
        print(f'{account.number}')
        print('Your card PIN:')
        print(f'{account.pin}')

    def login(self):
        """Implements user login to the account.
        It asks the client for the card number and pin,
        then reconciles the received data with existing accounts.
        If the entered data is found, displays a menu for the account."""

        print('Enter your card number:')
        number = input()
        print('Enter your PIN:')
        pin = input()
        # check the correctness of the entered data
        for account in self.accounts:
            if account.number == number:
                if account.pin == pin:
                    print('You have successfully logged in!\n')
                    self.current_account = account
                    self.menu(types='account')  # show submenu for customer account
                    return
        print('Wrong card number or PIN!\n')

    def show_balance(self):
        """Shows client balance"""
        print(f'Balance: {self.current_account.balance}')
        self.menu(types='account')

    def log_out(self):
        print('You have successfully logged out!\n')
        self.menu()  # shows main menu

    def run(self):
        """Main logic of the program"""
        while True:
            self.menu()
            # fulfill the wishes of the client
            if self.menu_choice == '1':
                self.create_account()
            elif self.menu_choice == '2':
                self.login()
            elif self.menu_choice == '2.1':
                self.show_balance()
            elif self.menu_choice == '2.2':
                self.log_out()
            else:
                print('Bye!')
                break


if __name__ == '__main__':
    banking = Banking()
    banking.run()
