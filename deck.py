import json
from card import Card

class Deck():
    def __init__(self):
        with open('deck.json') as data:
            cards = json.load(data)["cards"]
            self.number_of_cards = len(cards)
            self.suits = list(set([s.get("suit") for s in cards]))
            deck = []
            for c in cards:
                suit = c.get("suit")
                code = c.get("code")
                value = c.get("value")
                images = c.get("images")
                deck.append(Card(value, suit, code, images))
            self.deck = deck
            print(self.deck)



if __name__ == "__main__":
    deck = Deck()