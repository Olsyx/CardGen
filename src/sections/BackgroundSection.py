from src.sections.Section import *

class BackgroundSection(Section):

    def __init__(self, owner, structure):
        super().__init__(owner, structure)

    def write(self, card, structure, expand, debug, super_id = ""):
        if not self.check_available():
            return False

        style_class, section_class, composite_style = self.create_style(structure, expand, super_id)  

        html_body = '<div class="' + section_class + '"></div>'
        
        HtmlGenerator.store_style(style_class, composite_style.get_css(expanded=expand, debug=debug))
        HtmlGenerator.store_html(html_body)
        return False
