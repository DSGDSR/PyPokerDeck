# ![](/images/cards.png?raw=true "full!!!") PyPokerDeck

[![Issues](https://img.shields.io/github/issues/DSGDSR/pykedex.svg)](https://github.com/DSGDSR/PyPokerDeck/issues)
[![Stars](https://img.shields.io/github/stars/DSGDSR/pykedex.svg)](https://github.com/DSGDSR/PyPokerDeck/)
[![Tweet](https://img.shields.io/twitter/url/https/github.com/DSGDSR/pykedex.svg?style=social)](https://twitter.com/intent/tweet?text=Look%20what%20I%20just%20found%3A%20%F0%9F%83%8F%20PyPokerDeck%20for%20Python,%20a%20python%20simple%20deck%20manager%20at%20https%3A//github.com/DSGDSR/PyPokerDeck)
[![Follow on twitter](https://img.shields.io/twitter/follow/dsgdsrmc.svg?style=social&logo=twitter)](https://twitter.com/DSGDSRMC)

A python simple deck manager, using [Deck of Cards API](http://deckofcardsapi.com) images.

Maintainer: [DSGDSR](https://github.com/DSGDSR)

# Installation and usage
Clone repository:
```
$ git clone https://github.com/DSGDSR/PyPokerDeck.git
$ cd PyPokerDeck
```

# Usage
```
>>> deck = Deck(shuffle=True)                 # False by default
>>> deck.shuffle(times=2)                     # Custom shuffle (returns deck list)
>>> nc = deck.drawCards(2)                    # Draw 2 cards returning a list wiht them
>>> deck.reset()                              # Reset the deck without shuffling
>>> cc = deck.removeCard('8S')                # Removing a card returns its object
>>> sc = deck.searchCard('8S')                # Searching a card returns its object (None in case not found)
```

# Features

* Deck stored in json
* All cards with image, suit, code and value
* Deck shuffling
* Card drawing, remove or search
* Previews the sprite

# TODO

* Deploy as PyPi package
* Tests