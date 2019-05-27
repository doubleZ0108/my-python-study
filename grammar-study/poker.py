import random


class Card(object):
    def __init__(self, suit, figure):
        '''
        :param suit: 花色
        :param figure 点数
        '''
        self._suit = suit
        self._figure = figure

    @property
    def suit(self):
        return self._suit

    @property
    def figure(self):
        return self._figure

    def __str__(self):
        if self._figure == 1:
            figure_str = 'A'
        elif self._figure == 11:
            figure_str = 'J'
        elif self._figure == 12:
            figure_str = 'Q'
        elif self._figure == 13:
            figure_str = 'K'
        else:
            figure_str = str(self._figure)

        return '%s%s' % (self._suit, figure_str)

    def __repr__(self):
        return self.__str__()


class Poker(object):
    def __init__(self):
        self._cards = [Card(suit, figure) for suit in '♠♥♣♦' for figure in range(1, 14)]
        self._current = -1

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        '''洗牌（随机乱序）'''
        random.shuffle(self._cards)

    def next(self):
        self._current += 1
        if not self.isEnd():
            return self._cards[self._current]
        else:
            return -1

    def isEnd(self):
        return self._current > len(self._cards)


class Player(object):
    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        '''玩家整理自己的手牌'''
        self._cards_on_hand.sort(key=card_key)


# 排序规则 => 先根据点数再根据花色
def get_key(card):
    return (card.figure, card.suit)


def main():
    p = Poker()
    p.shuffle()
    players = [Player('zz'), Player('yt'), Player('gf'), Player('sm')]
    for _ in range(13):
        for player in players:
            player.get(p.next())

    for player in players:
        print(player.name, end=' ')
        player.arrange(get_key)
        print(player.cards_on_hand)


if __name__ == '__main__':
    main()
