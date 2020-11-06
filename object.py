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


class Hand():

  def __init__(self, dealer=False):
    self.dealer = dealer
    self.cards = []
    self.total = 0

  def add_card(self, card):
    self.cards.append(card)

  def calc_value(self):
    self.value = 0
    ace = False
    for card in self.cards:
      self.value += int(card.number['value'])
      if card.number['key'] == 'A':
        ace = True

    if ace and self.value > 21:
      self.value -= 10

    return self.value

  def is_blackjack(self):
    return self.calc_value() == 21

  def show(self, show_two_cards=False):
    if self.dealer is True:
      print('Dealer hand:')
    else:
      print('Your hand:')

    # print(f"{'Dealer' if self.dealer else 'Your'} hand:")

    for index, card in enumerate(self.cards):
      if index == 0 and self.dealer and not show_two_cards and not self.is_blackjack():
        pass
      else:
        print(f"{card.suit} {card.number['key']}")
    if not self.dealer:
      print('Total:', self.calc_value())
    print()

class Game():

  def check_winner(self, player_hand, dealer_hand, game_over=False):
    if not game_over:
      if player_hand.calc_value() > 21:
        print('あなたは21を超えました. Dealer wins!')
        return True
      elif dealer_hand.calc_value() > 21:
        print('ディーラーは21を超えました. You win!')
        return True
      elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
        print('ふたりともブラックジャックです. Draw!')
        return True
      elif player_hand.is_blackjack():
        print('あなたはブラックジャックです! You win!')
        return True
      elif dealer_hand.is_blackjack():
        print('ディーラーはブラックジャックです! Dealer wins!')
        return True
    else:
      if player_hand.calc_value() > dealer_hand.calc_value():
          print('You win!')
      elif player_hand.calc_value() == dealer_hand.calc_value():
          print('Draw!')
      else:
          print('Dealer wins!')
      return True
    return False


  def play(self):
    game_to_play = 0

    while game_to_play <= 0:
      try:
        game_to_play = int(input('何回ゲームをプレイしますか？:'))
      except ValueError:
        print('数字で入力してください。')

game = Game()
game.play()

deck = Deck()
deck.shuffle()

player_hand = Hand()
dealer_hand = Hand(dealer=True)

for i in range(2):
  player_hand.add_card(deck.deal())
  dealer_hand.add_card(deck.deal())

player_hand.show()
dealer_hand.show()