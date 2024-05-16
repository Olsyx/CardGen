from src.IO import *

class HtmlGenerator:
    page_css_name = ""
    page_css_path = ""
    html_file_path = ""
    css_file_path = ""

    html = ""
    styles = {}
    tabs = 0

    @staticmethod
    def clear():
        HtmlGenerator.html = ""
        HtmlGenerator.styles = {}
        HtmlGenerator.tabs = 0

    @staticmethod
    def init(out_path): 
        HtmlGenerator.clear()

        HtmlGenerator.page_css_name = os.path.basename(out_path) + "-" + "page-style.css"
        HtmlGenerator.html_file_path = out_path + ".html"
        HtmlGenerator.css_file_path = out_path + ".css"
        HtmlGenerator.page_css_path = os.path.normpath(os.path.join(os.path.dirname(HtmlGenerator.html_file_path), HtmlGenerator.page_css_name))

        IO.open_file("PageCss", HtmlGenerator.page_css_path, "w")
        IO.open_file("HTML", HtmlGenerator.html_file_path, "w")
        IO.open_file("Style", HtmlGenerator.css_file_path, "w")
        HtmlGenerator.write_heading()

    @staticmethod
    def end():
        HtmlGenerator.write_page_style()
        IO.end("PageCss")
        HtmlGenerator.write_html()
        IO.end("HTML")
        HtmlGenerator.write_style()
        IO.end("Style")

    @staticmethod
    def write_page_style():
        page_css =  ".page-content {\n"
        page_css += "\tdisplay: flex;\n"
        page_css += "\tflex-direction: row;\n"
        page_css += "\tjustify-content: space-between;\n"
        page_css += "\tflex-wrap: wrap;\n"
        page_css += "\twidth: auto;\n"
        page_css += "\theight: auto;\n"
        page_css += "}"
        
        IO.write_to("PageCss", page_css)

    @staticmethod
    def write_html():
        IO.write_to("HTML", HtmlGenerator.html)
        HtmlGenerator.write_ending()
        
    @staticmethod
    def write_style():
        for s in HtmlGenerator.styles:
            IO.write_to("Style", HtmlGenerator.styles[s])

    @staticmethod
    def write_heading():
        HtmlGenerator.store_html("<!DOCTYPE html>")
        HtmlGenerator.store_html("<html>")
        HtmlGenerator.add_tab()
        HtmlGenerator.store_html("<head>")
        HtmlGenerator.add_tab()
        HtmlGenerator.store_html('<link rel="stylesheet" type="text/css" href="fonts.css">')
        HtmlGenerator.store_html('<link rel="stylesheet" type="text/css" href="' + HtmlGenerator.page_css_name + '">')
        HtmlGenerator.store_html('<link rel="stylesheet" type="text/css" href="' + os.path.basename(HtmlGenerator.css_file_path) + '">')
        HtmlGenerator.remove_tab()
        HtmlGenerator.store_html("</head>")
        HtmlGenerator.store_html("<body>")
        HtmlGenerator.add_tab()
        HtmlGenerator.store_html('<div class="page-content">')

    @staticmethod
    def write_ending():
        HtmlGenerator.remove_tab()
        HtmlGenerator.store_html('</div>')
        HtmlGenerator.remove_tab()
        HtmlGenerator.store_html("</body>")
        HtmlGenerator.remove_tab()
        HtmlGenerator.store_html("</html>")

    @staticmethod
    def get_tabs():
        return HtmlGenerator.tabs * "\t"

    @staticmethod
    def add_tab():
        HtmlGenerator.tabs = HtmlGenerator.tabs + 1

    @staticmethod
    def remove_tab():
        HtmlGenerator.tabs = HtmlGenerator.tabs - 1
 
    @staticmethod
    def store_html(text):
        if text is None:
            return

        HtmlGenerator.html += HtmlGenerator.get_tabs() + text + "\n"
        

    @staticmethod
    def store_style(class_name, attributes):
        if class_name is None or attributes is None:
            return
         
        text = "." + class_name + " {\n"
        text += attributes
        text += "}\n\n"
        
        HtmlGenerator.styles[class_name] = text
