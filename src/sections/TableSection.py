from src.sections.Section import *

class TableSection(Section):

    inside_styles = []

    def __init__(self, owner, structure):
        super().__init__(owner, structure)

        for entry in structure:
            self.inside_styles.append(entry)



    def write(self, card, structure, expand, debug, super_id = ""):
        if not self.check_available():
            return True
        
        content = ""
        if structure is None:
            if not debug:
                return True # expand next section
        else:
            content = structure.text
        
        style_class, section_class, composite_style = self.create_style(structure, expand, super_id)  
        
        self.store_style(style_class, composite_style, expand, debug)

        HtmlGenerator.store_html('<table class="' + section_class + '">')
        HtmlGenerator.add_tab()
        
        for row in structure:
            HtmlGenerator.add_tab()
            HtmlGenerator.add_tab()
            HtmlGenerator.store_html('<' + row.tag + '>')

            for col in row:
                HtmlGenerator.store_html('<' + col.tag + '>' + self.parse_content(col.text) + '</' + col.tag + '>')
            
            HtmlGenerator.store_html('</' + row.tag + '>')
            HtmlGenerator.remove_tab()
            HtmlGenerator.remove_tab()

        HtmlGenerator.remove_tab()
        HtmlGenerator.store_html("</table>")
        return False

    def store_style(self, style_class, composite_style, expand, debug):        
        HtmlGenerator.store_style(style_class, composite_style.get_css(expanded=expand, debug=debug))

        for entry in self.inside_styles:
            label = entry.tag
            id = entry.get("id")

            if id is not None:
                label += ":" + id

            style = Style(entry)
            HtmlGenerator.store_style(style_class + " " + label, style.get_css(expanded=expand, debug=debug))
        
            