# JetBrains Academy/Python Developer
# Project: Simple Banking System
# Stage 1/4: Card anatomy

from random import sample, randint
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
        self.id = int(datetime.today().strftime("%d%H%M%S")) + randint(10, 20) * 10  # generator of account identifier
        self.number = str(4000000000000000 + self.id)            # generator of number of the card
        self.pin = ''.join(map(str, sample(range(0, 9), 4)))     # generator of random 4 digits pin code


class Menu:
    """Menu of the program"""
    def __init__(self):
        self.__choice = '0'

    def __repr__(self):
        return self.__choice

    def __eq__(self, other):
        return True if self.__choice == other else False

    @staticmethod
    def __show_main_menu():
        print('1. Create an account')
        print('2. Log into account')
        print('0. Exit')

    @staticmethod
    def __show_account_menu():
        print('1. Balance')
        print('2. Log out')
        print('0. Exit')

    def show_and_get_choice(self):
        if self.__choice.startswith('2'):
            self.__show_account_menu()
            self.__choice = f'{self.__choice[0]}.{input()}'
        else:
            self.__show_main_menu()
            self.__choice = input()

    def back_to_main(self):
        self.__choice = '0'


class Banking:
    """Banking system"""
    def __init__(self):
        self.menu = Menu()
        self.current_account = None
        self.accounts = {}  # temporary dict (database) for accounts

    def create_account(self):
        """Creates a customer account"""
        account = Account()
        self.accounts[account.id] = account  # temporary solution
        # show the result according to the condition of the task
        print('Your card has been created')
        print('Your card number:')
        print(f'{self.accounts[account.id].number}')
        print('Your card PIN:')
        print(f'{self.accounts[account.id].pin}\n')

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
        for account in self.accounts.values():
            if account.number == number:
                if account.pin == pin:
                    print('You have successfully logged in!\n')
                    self.current_account = account
                    return
        print('Wrong card number or PIN!\n')
        self.menu.back_to_main()

    def show_balance(self):
        """Shows client balance"""
        print(f'Balance: {self.current_account.balance}\n')

    def log_out(self):
        """Shows the main menu, allowing the client to log in with another account."""
        print('You have successfully logged out!\n')
        self.menu.back_to_main()

    def run(self):
        """Main logic of the program"""
        while True:
            self.menu.show_and_get_choice()
            # fulfill the wishes of the client
            if self.menu == '1':
                self.create_account()
            elif self.menu == '2':
                self.login()
            elif self.menu == '2.1':
                self.show_balance()
            elif self.menu == '2.2':
                self.log_out()
            else:
                print('Bye!')
                break


if __name__ == '__main__':
    banking = Banking()
    banking.run()
