from random import shuffle
from enum import Enum, unique

@unique
class Suite(Enum):
    """花色"""
    
    SPADE, HEART, CLUB, DIAMOND = range(4)

    def __lt__(self, other):    # 判断self对象是否小于other对象
        return self.value<other.value

class Card(object):
    """一张牌"""
    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def suite(self):
        return self._suite

    @property
    def face(self):
        return self._face

    def __str__(self):
        suites = ['♠️', '♥️', '♣️', '♦️']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self._suite.value]} {faces[self._face]}'

    def __repr__(self):
        return self.__str__()

class Poker(object):
    """一副牌"""
    def __init__(self):
        self._card = [Card(suite,face) for suite in Suite for face in range(1,14)]
        self._current = 0

    def shuffle(self):
        self._current = 0
        shuffle(self._card)

    @property
    def has_next(self):
        return self._current < len(self._card)

    def next(self):
        card = self._card[self._current]
        self._current += 1
        return card
    

class Player(object):
    """玩家"""
    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name
        
    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get_one(self, card):
        self._cards_on_hand.append(card)

    def sort(self, cmp=lambda card: (card.suite, card.face)):
        self._cards_on_hand.sort(key=cmp)

def main():
    poker = Poker()
    poker.shuffle()
    players = [Player('东邪'),Player('西毒'),Player('南帝'),Player('北丐')]
    while poker.has_next:
        for player in players:
            player.get_one(poker.next())
    for player in players:
        player.sort()
        print(player.name,end=': ')
        print(player.cards_on_hand)

if __name__ == "__main__":
    main()
