import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4


def deal():
  hand = []
  for i in range(2):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:
      card = "J"
    if card == 12:
      card = "Q"
    if card == 11:
      card = "K"
    if card == 1:
      card = "A"
    hand.append(card)
  return hand


def hit(hand):
  random.shuffle(deck)
  card = deck.pop()
  if card == 11:
    card = "J"
  if card == 12:
    card = "Q"
  if card == 11:
    card = "K"
  if card == 1:
    card = "A"
  hand.append(card)
  return hand


def total(hand):
  score = 0
  for card in hand:
    if card == "J" or card == "Q" or card == "K":
      score = score + 10
    elif card == "A":
      if score >= 11:
        score = score + 1
      else:
        score += 11
    else:
      score += card 
  return score


def play_again():
  again = input("もう１度プレイしますか？　(Y/N): ")
  if again == "y" or again == "Y":
    # game()
    return
  else:
    print("お疲れ様でした！")
    exit()


def game():
  dealer_hand = deal()
  player_hand = deal()
  print(f"ディーラーは{dealer_hand[0]}です")
  print(f"プレイヤーは{player_hand}です")
  print(total(dealer_hand))
  print(total(player_hand))


game()