
class Card:
    id = ""
    card_type = ""
    attributes = {}

    def __init__(self, structure):
        self.id = structure.get("id")
        self.card_type = structure.get("card-type")
        
        self.attributes = {}
        for entry in structure:
            self.attributes[entry.tag] = entry