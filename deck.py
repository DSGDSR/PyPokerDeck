import json, random
from card import Card

class Deck():
    def __init__(self):
        with open('deck.json') as data:
            cards = json.load(data)["cards"]
            self.number_of_cards = len(cards)
            self.suits = list(set([s.get("suit") for s in cards]))
            self.codes = [s.get("code") for s in cards]
            self.shuffled = False
            deck = []
            for c in cards:
                suit = c.get("suit")
                code = c.get("code")
                value = c.get("value")
                images = c.get("images")
                deck.append(Card(value, suit, code, images))
            self.deck = deck

    def drawCards(self, t):
        cards = self.deck[self.number_of_cards-t:]
        [self.deck.pop() for _ in range(0,t)]
        self.number_of_cards = len(self.deck)
        return cards

    def shuffle(self, t):
        [random.shuffle(self.deck) for _ in range(0,t)]
        self.shuffled = True
        return self.deck

    def reset(self):
        self.__init__()

    def searchCard(self, code):
        for c in self.deck:
            if code == c.get("code"):
                return True

    def removeCard(self, code):
        if code in self.codes:
            for c in self.deck:
                if code == c.code:
                    self.deck.remove(c)
                    self.number_of_cards = len(self.deck)
                    return True
        else:
            return False



if __name__ == "__main__":
    deck = Deck()
    deck.shuffle(5)
    nc = deck.drawCards(2)
    nc = deck.drawCards(3)
    print([c.code for c in nc], deck.number_of_cards, "\n")

    deck.reset()
    print([c.code for c in deck.deck], deck.number_of_cards, "\n")

    if deck.removeCard('8S'):
        print("8S removed")
    else:
        print("Error")
    print([c.code for c in deck.deck], deck.number_of_cards, "\n")