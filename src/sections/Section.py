from src.HtmlGenerator import *

from src.Style import *
import copy
import re

ADAPTED_CARDS = 0

class Section:
    owner = ""
    id = ""
    section_type = ""

    template_style = ""
    super_style = None
    style = None
    structure = None
    check_section_available = ""

    line_break_pattern = re.compile(r"\n[ ]+")
    bold_pattern = re.compile(r"\*\*[ ]+\*\*")


    def __init__(self, owner, structure):
        self.owner = owner
        self.id = structure.get("id")
        self.template_style = structure.get("style")
        self.structure = structure
        self.section_type = structure.tag
        self.style = Style(structure)
        self.check_section_available = structure.get("only-if")

    def set_super(self, super_id):
        self.id = super_id + "_" + self.id
        
    def write(self, card, content, expand, debug, super_id = ""):
        return False
    
    def check_available(self):
        if self.check_section_available is "" or self.check_section_available is None:
            return True
        
        return self.check_section_available in self.owner.writing_card.attributes

    # ---------------- CONTENT PARSING ---------------- #
    def parse_content(self, text):
        if text is None:
            return ""
        
        text = self.line_break_pattern.sub("<br/>", text)
        text = text.replace("\\n", "<br/>")
        text = text.replace(" ", "&nbsp;")
        text = text.replace("\\t", "&emsp;")
        text = self.replace_markdown(text, "**", "b")
        text = self.replace_markdown(text, "__", "i")

        for id in self.owner.style_markers:
            marker = self.owner.style_markers[id]
            text = self.replace_markdown(text, marker.symbol, "span", id)
        return text

    def replace_markdown(self, text, mark, label, apply_class = ""):

        start_label = "<" + label 
        if apply_class != "":
            start_label += " class=\"" + apply_class + "\""
        start_label += ">"
        
        end_label = "</" + label + ">"

        index = text.find(mark)
        start = True
        while index >= 0:
            label = ""
            if start:
                label = start_label
            else:
                label = end_label
            start = not start
            text = text[:index] + label + text[index+len(mark):]
            index = text.find(mark)

        return text

    def create_style(self, structure, expand, super_id):
        full_id = self.id
        if super_id is not "":
            full_id = super_id + "_" + full_id

        composite_style = copy.deepcopy(self.style)

        # -- Define Style --
        style_class = self.owner.card_type + " ." + full_id
        section_class = full_id

        # -- Get Template Style --
        if self.template_style is not None and self.template_style != "":
            new_style = Style(self.owner.style_templates[self.template_style])
            new_style.add(composite_style)
            composite_style = new_style
            
        # -- Add Custom Structure Style --
        if structure is not None:
            structure_style = Style(structure) 

            if not structure_style.is_empty():
                composite_style.add(structure_style)

                print("applying structure style to <" + full_id + ">")

                global ADAPTED_CARDS
                style_class += "-adapted" + str(ADAPTED_CARDS)
                section_class += "-adapted" + str(ADAPTED_CARDS)
                ADAPTED_CARDS += 1
            
        # -- Add Expanded --
        if expand:
            style_class += "-expanded"
            section_class += "-expanded"
        

        return style_class, section_class, composite_style


