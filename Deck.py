from const import printed, suits, ranks
from intertools import product

class Card:

    def __init__(self, suit, rank, picture, points):
        self.suit = suit
        self.rank = rank
        self.points = points
        self.picture = picture

    def __str__(self):
        message = self.picture + '\nPoints: ' + str(self.points)
        return message


class Deck:

    def __init__(self):
        self.cards = self._create_deck()
        shuffle(self.cards)

#изменить, должен быть визуальный вывод карт на доске
    def _create_deck(self):
        cards = []
        for suit, rank in product(suits, ranks):
            if rank == 'ace':
                points = 11
            elif rank.isdigit():
                points = int(rank)
            else:
                points = 10

            picture = printed.get(rank)

            c = Card(suit=suit, rank=rank, points=points, picture=picture)
            cards.append(c)
        return cards

    def get_card(self):
         return self.cards.pop()

    def __len__(self):
        return len(self.cards)