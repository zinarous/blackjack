from Deck import Deck
from Game import Game
from Player import Bot

def start_g():
    g = Game()
    g.start_game()
    print('Количество ваших денег: ', g.player.money)
    # if r is not None and r == 0:
    #     return False

