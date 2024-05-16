from src.sections.Section import *

class ImageSection(Section):

    def __init__(self, owner, structure):
        super().__init__(owner, structure)

    def write(self, card, structure, expand, debug, super_id = ""):
        if not self.check_available():
            return True
        
        content = ""
        if structure is None:
            content = ""
        else:
            content = structure.text
                
        style_class, section_class, composite_style = self.create_style(structure, expand, super_id)

        # -- HTML Generation --
        HtmlGenerator.store_style(style_class, composite_style.get_css(expanded=expand, debug=debug))

        HtmlGenerator.store_html('<div class="' + section_class + '">')
        HtmlGenerator.add_tab()
        HtmlGenerator.store_style(section_class + " img" , composite_style.get_adaptive_img_css())
        HtmlGenerator.store_html('<img src="' + self.parse_content(content) + '"/>')
        HtmlGenerator.remove_tab()
        HtmlGenerator.store_html("</div>")
        
        return False
