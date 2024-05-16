import copy
from src.sections.Section import *
from src.SectionFactory import *

SECTION_FACTORY = SectionFactory()

class Side:        
    card_type = ""
    side = ""
    style = None
    sections = {}
    style_markers = {}
    style_templates = {}
    writing_card = None

    def __init__(self, card_type, structure):
        global SECTION_FACTORY

        self.card_type = card_type
        self.side = structure.tag
        self.style = Style(structure)
        
        self.sections = {}
        self.style_templates = {}
        for entry in structure:
            section = SECTION_FACTORY.build(self, entry)

            if entry.tag == "style":
                self.style_templates[entry.get("id")] = entry
            elif entry.tag == "marker":
                self.style_markers[entry.get("id")] = Style(entry)
            else:
                self.sections[section.id] = section

    
    def write(self, card, debug=False):
        side_class = self.card_type + "." + self.side
        HtmlGenerator.store_style(side_class, self.style.get_css(debug=debug))

        for id in self.style_markers:
            marker = self.style_markers[id]
            HtmlGenerator.store_style(side_class + " ." + id, marker.get_css(debug=debug))

        div_class = self.card_type + " " + self.side
        HtmlGenerator.store_html('<div class="' + div_class + '">')
        HtmlGenerator.add_tab()
        
        self.write_sections(card, debug)
            
        HtmlGenerator.remove_tab()
        HtmlGenerator.store_html("</div>")
        
    def write_sections(self, card, debug=False):
        self.writing_card = card
        expand = False
        for key in self.sections:
            content = None
            if key in self.writing_card.attributes:
                content = self.writing_card.attributes[key]
            expand = self.sections[key].write(self.writing_card, content, expand, debug)

    def show(self, debug=False):     
        HtmlGenerator.store_style(self.card_type, self.style.get_css(debug=debug))

        div_class = self.card_type + " " + self.side 
        HtmlGenerator.store_html('<div class="' + div_class + '">')
        HtmlGenerator.add_tab()
        
        for s in self.sections:
            s.show()
            
        HtmlGenerator.remove_tab()
        HtmlGenerator.store_html("</div>")