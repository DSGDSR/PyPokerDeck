import json, random
from card import Card

class Deck():
    def __init__(self, shuffle=False):
        with open('deck.json') as data:
            cards = json.load(data)["cards"]
            self.number_of_cards = len(cards)
            self.suits = list(set([s.get("suit") for s in cards]))
            self.codes = [s.get("code") for s in cards]
            self.shuffled = shuffle
            deck = []
            for c in cards:
                suit = c.get("suit")
                code = c.get("code")
                value = c.get("value")
                images = c.get("images")
                deck.append(Card(value, suit, code, images))
            self.deck = deck
            if self.shuffled:
                self.shuffle()

    def drawCards(self, t):
        cards = self.deck[self.number_of_cards-t:]
        [self.deck.pop() for _ in range(0,t)]
        self.number_of_cards = len(self.deck)
        return cards

    def shuffle(self, times=1):
        [random.shuffle(self.deck) for _ in range(0,times)]
        self.shuffled = True
        return self.deck

    def reset(self):
        self.__init__()

    def searchCard(self, code):
        for c in self.deck:
            if code == c.get("code"):
                return c
        return None

    def removeCard(self, code):
        if code in self.codes:
            for c in self.deck:
                if code == c.code:
                    self.deck.remove(c)
                    self.number_of_cards = len(self.deck)
                    return c
        else:
            return False



if __name__ == "__main__":
    deck = Deck(shuffle=True)

    # Custom shuffle
    deck.shuffle(times=2)

    # Draw 2 cards returning a list wiht them
    nc = deck.drawCards(2)

    # Reset the deck without shuffling
    deck.reset()

    # Removing a card returns its object
    cc = deck.removeCard('8S')
    print("8S removed", cc.code)

    # Searching a card returns its object
    # (None in case not found)
    sc = deck.searchCard('8S')