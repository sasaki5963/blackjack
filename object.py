import random

class Card():
  def __init__(self, suit, number):
    self.suit = suit
    self.number = number

  def __repr__(self):
    return f'{self.suit} {self.number}'

trump = Card('❤︎',10)
print(trump)

class Deck():

  def __init__(self):
    suits = ['♠︎', '❤︎', '♣︎', '♦︎']
    numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']

    self.cards = []

    for suit in suits:
      for number in numbers:
        self.cards.append(Card(suit, number))

  def deal(self):
    return self.cards.pop()

  def shuffle(self):
    random.shuffle(self.cards)

print(Deck().cards)

hand = Deck().deal()
print(hand)

dekki = Deck()
dekki.shuffle()
hand2 = dekki.deal()
print(hand2)