import random

class Card():
  def __init__(self, suit, number):
    self.suit = suit
    self.number = number

  def __repr__(self):
    return f'{self.suit} {self.number}'

class Deck():

  def __init__(self):
    suits = ['♠︎', '❤︎', '♣︎', '♦︎']
    numbers = [
      {'key': 'A', 'value': 11},
      {'key': '2', 'value': 2},
      {'key': '3', 'value': 3},
      {'key': '4', 'value': 4},
      {'key': '5', 'value': 5},
      {'key': '6', 'value': 6},
      {'key': '7', 'value': 7},
      {'key': '8', 'value': 8},
      {'key': '9', 'value': 9},
      {'key': '10', 'value': 10},
      {'key': 'J', 'value': 10},
      {'key': 'Q', 'value': 10},
      {'key': 'K', 'value': 10},
    ]

    self.cards = []

    for suit in suits:
      for number in numbers:
        self.cards.append(Card(suit, number))

  def deal(self):
    return self.cards.pop()

  def shuffle(self):
    random.shuffle(self.cards)

trump = Deck().deal()
print(trump)
print(trump.number)
print(trump.number['key'])
print(trump.number['value'])