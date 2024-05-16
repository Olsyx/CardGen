from src.sections.Section import *

class TextSection(Section):

    def __init__(self, owner, structure):
        super().__init__(owner, structure)

    def write(self, card, structure, expand, debug, super_id = ""):
        if not self.check_available():
            return True
        
        content = ""
        if structure is None:
            if not debug:
                return True # expand next section
        else:
            content = structure.text
       
        self.style.display = "flex" # Text must be flex for vertical alignment. It sucks, I know.            

        style_class, section_class, composite_style = self.create_style(structure, expand, super_id)

        # -- HTML Generation --
        HtmlGenerator.store_style(style_class, composite_style.get_css(expanded=expand, debug=debug))
        HtmlGenerator.store_html('<div class="' + section_class + '">')
        HtmlGenerator.add_tab()

        if composite_style.deform != None and composite_style.deform != "":
            composite_style.generate_span_deforms(style_class, content)
            for index, char in enumerate(content):
                HtmlGenerator.store_html('<span class="char' + str(index) + '">' + char + '</span>')
        else:
            HtmlGenerator.store_html('<span>' + super().parse_content(content) + '</span>')

        HtmlGenerator.remove_tab()
        HtmlGenerator.store_html("</div>")

        
        return False