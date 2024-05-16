from src.IO import *
import re
import json
import shutil

FONTS_PATH = "./fonts.css"
FONTS_JSON = "./fonts.json"

class Fonts:

    _ = {}

    @staticmethod
    def init(output_folder): 
        global FONTS_PATH       
        if output_folder is not None and output_folder != "":
            FONTS_PATH = os.path.join(output_folder, FONTS_PATH)

        fonts_folder_path = output_folder + "/fonts"
        if os.path.isdir(fonts_folder_path):
            shutil.rmtree(fonts_folder_path)
        shutil.copytree(os.getcwd() + "\\fonts", output_folder + "/fonts" )
        Fonts.create_css()
        Fonts.store_()

    @staticmethod
    def create_css():
        global FONTS_PATH
        IO.open_file("FontsJson", FONTS_JSON, "r")
        json_data = json.loads(IO.read("FontsJson"))
        IO.end("FontsJson")

        full_css = ""
        for key in json_data:
            entry = json_data[key]
            
            if "regular" in entry:
                full_css += Fonts.create_font_css(key, entry["regular"], False, False) + "\n"
            
            if "bold" in entry:
                full_css += Fonts.create_font_css(key, entry["bold"], False, True) + "\n"
                
            if "italic" in entry:
                full_css += Fonts.create_font_css(key, entry["italic"], True, False) + "\n"
                
            if "italic_bold" in entry:
                full_css += Fonts.create_font_css(key, entry["italic_bold"], True, True) + "\n"

        IO.open_file("Fonts", FONTS_PATH, "w")
        IO.write_to("Fonts", full_css)
        IO.end("Fonts")

    @staticmethod
    def create_font_css(font_name, font_url, italic, bold):   
        css = '@font-face {\n'
        css += '\tfont-family: "' + font_name + '";\n'
        css += '\tsrc: url("' + font_url + '");\n'

        if italic:
            css += "\tfont-style: italic;\n"
        
        if bold:
            css += "\tfont-weight: bold;\n"

        return css + '}\n'

    @staticmethod
    def store_():
        global FONTS_PATH
        IO.open_file("Fonts", FONTS_PATH, "r")
        fonts_file = IO.read("Fonts")
        IO.end("Fonts")

        font_names = re.findall(r'font-family:(.*);', fonts_file)
        urls = re.findall(r'url\((.*)\);', fonts_file)

        for i in range(0, len(font_names)):
            Fonts._[font_names[i].replace('"', '').replace(' ', '')] = urls[i].replace('\\ ', ' ')

    @staticmethod
    def get_url(font_name):
        return Fonts._[font_name.replace(' ', '')]
    
    def print_():
        for key in Fonts._:
            print(key, ",", Fonts._[key])