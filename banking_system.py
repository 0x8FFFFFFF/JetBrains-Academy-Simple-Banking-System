from random import sample


class Card:
    id = 0  # INTEGER
    number = ''  # TEXT
    pin = ''   # TEXT
    balance = 0  # INTEGER DEFAULT 0

    def __init__(self, _id):
        self.id = _id
        self.number = str(4000000000000000 + self.id)
        self.pin = ''.join(map(str, sample(range(0, 9), 4)))


class Account:
    pass


class Banking:
    def __init__(self):
        self.accounts = {}

    def menu(self):
        print('1. Create an account')
        print('2. Log into account')
        print('0. Exit')
        self.menu_choice = int(input())

    def create_account(self):
        pass

    def login(self):
        pass
