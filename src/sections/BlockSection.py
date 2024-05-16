from src.sections.Section import *

class BlockSection(Section):

    inside_sections = {}

    def __init__(self, owner, structure, factory):
        super().__init__(owner, structure)

        self.inside_sections = {}
        for entry in structure:
            section = factory.build(self.owner, entry)
                
            if entry.tag != "style":
                self.inside_sections[section.id] = section
            else:
                self.owner.style_templates[section.id] = section

    def write(self, card, structure, expand, debug, super_id = ""):
        if not self.check_available():
            return True
        
        style_class, section_class, composite_style = self.create_style(structure, expand, super_id)      

        HtmlGenerator.store_style(style_class, composite_style.get_css(expanded=expand, debug=debug))

        HtmlGenerator.store_html('<div class="' + section_class + '">')
        HtmlGenerator.add_tab()
        
        full_id = section_class

        expand = False
        for key in self.inside_sections:            
            content = None
            if key in card.attributes:
                content = card.attributes[key]     

            section = self.inside_sections[key]
            expand = section.write(card, content, expand, debug, full_id)

        HtmlGenerator.remove_tab()
        HtmlGenerator.store_html("</div>")
        return False
