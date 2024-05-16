from src.sections.TextSection import *
from src.sections.ImageSection import *
from src.sections.BackgroundSection import *
from src.sections.TableSection import *
from src.sections.FlexboxSection import *
from src.sections.BlockSection import *

class SectionFactory():
    
    def build(self, card_side, entry):        
        if entry.tag == "text":
            return TextSection(card_side, entry)
        elif entry.tag == "image":
            return ImageSection(card_side, entry)
        elif entry.tag == "background":
            return BackgroundSection(card_side, entry)
        elif entry.tag == "table":
            return TableSection(card_side, entry)
        elif entry.tag == "flexbox":
            return FlexboxSection(card_side, entry, self)
        elif entry.tag == "block":
            return BlockSection(card_side, entry, self)

        return None
