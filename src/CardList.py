from src.IO import *
from src.Card import *

class CardList:
    cards = {}

    @staticmethod
    def load(path):        
        tree = IO.read_xml(path, path)
        CardList.cards = {}
        for elem in tree:
            CardList.cards[elem.get("id")] = Card(elem)

    @staticmethod
    def get_card(id):
        return CardList.cards[id]