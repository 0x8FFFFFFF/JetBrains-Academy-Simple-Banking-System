from datetime import datetime


class Card:
    id = 0  # INTEGER
    number = ''  # TEXT
    pin = ''   # TEXT
    balance = 0  # INTEGER DEFAULT 0

    def __init__(self, _id):
        self.id = _id
        self.number = '400000' + datetime.today().strftime('%Y%')
