from src.Side import *
from src.HtmlGenerator import *
from src.Style import *

class Template:    
    card_type = ""
    style = None
    sides = []
    card_separation = 2

    def __init__(self, structure):
        self.card_type = structure.get("card-type")
        self.style = Style(structure)
                   
        self.sides = []
        for line in structure:
            self.sides.append(Side(self.card_type, line))
            
        HtmlGenerator.store_style("card-wrapper", self.get_wrapper_style())

    def write_card(self, card, debug=False):
        HtmlGenerator.store_style(self.card_type, self.style.get_css(debug=debug))

        HtmlGenerator.store_html('<div class="card-wrapper">')
        HtmlGenerator.add_tab()

        for s in self.sides:
            s.write(card, debug)
 
        HtmlGenerator.remove_tab()
        HtmlGenerator.store_html('</div>')

    def get_wrapper_style(self):
        style = "\tdisplay: flex;\n"
        style += "\tflex-direction: row;\n"
        style += "\tjustify-content: space-between;\n"
        style += "\tbreak-inside: avoid;\n"   # Avoid div getting cut off when printing
        style += "\twidth: " + str(float(self.style.width) * len(self.sides) + Template.card_separation) + "mm;\n"
        style += "\theight: " + str(float(self.style.height) + Template.card_separation) + "mm;\n"
        return style
    # ---------------- TEMPLATE SHOWING ---------------- #
    def show(self, debug=False):
        for s in self.sides:
            s.show(debug)
        
