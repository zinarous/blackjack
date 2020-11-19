from Deck import Deck

if __name__ == '__main__':
    d = Deck()

    print(len(d))
    card = d.get_card()
    print(card)
    print(len(d))