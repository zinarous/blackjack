import abc
from Deck import Deck
import random

class AbstractPlayer(abc.ABC):

    def __init__(self, position):
        self.cards = []
        self.position = position #позиция игрока
        self.bet = 0
        self.full_points = 0

    def change_points(self):
        self.full_points = sum([card.points for card in self.cards])
    
    def ask_card(self, deck, card_count):
        for _ in range(card_count):    
            card = deck.get_card()
            self.cards.append(card)
        self.change_points()
        return True

    @abc.abstractmethod
    def change_bet(self, max_bet, min_bet):
        pass

    def print_cards(self):
        print(self, 'Информация по игроку')
        for card in self.cards:
            print(card)
        print(self.full_points)


class Player(AbstractPlayer):

    def change_bet(self, max_bet, min_bet):
        while True:
            value = int(input('Сделайте свою ставку: '))
            if value < max_bet and value > min_bet:
                self.bet = value
                break
        print('Ваша ставка: ', self.bet)

#class Dealler(AbstractPlayer):

class Bot(AbstractPlayer):

    def change_bet(self, max_bet, min_bet):
        self.bet = random.randint(min_bet, max_bet)
        print(self, 'дана: ', self.bet)