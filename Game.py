import Player

from Deck import Deck
from const import MESSAGES
import random

class Game:

    def __init__(self):
        self.players = []
        self.player = None
        #self.dealler = None
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 0
        

    #должна быть ссылка на кнопку Начать игру
    @staticmethod
    def _ask_starting(message):
        while True:
            choice = input(message)
            if choice == 'н':
                return False
            elif choice == 'д':
                return True

    def _launching(self):
        bots_count = int(input('Напишите количество дополнительных игроков '))
        self.all_players_count = bots_count + 1

        for i in range(bots_count):
            b = Player.Bot(position=i)
            self.players.append(b)
            
            print(b, ' создан')

        self.player = Player.Player(position=bots_count + 1)
        self.players.append(self.player)

    def ask_bet(self):
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)

    def first_descr(self):
        for player in self.players:
            player.ask_card(self.deck, 2)


    def start_game(self):
        message = MESSAGES.get('ask_start')
        if not self._ask_starting(message=message):
            exit(1)

        #подготовка данных для начала
        self._launching()

        self.ask_bet()

        #выдача первых карт для игроков
        self.first_descr()

Game.asd = 10
        