from src.IO import *
from src.Template import *

class TemplateSet:
    templates = {}

    @staticmethod
    def load(path):        
        tree = IO.read_xml(path, path)
        TemplateSet.templates = {}
        for elem in tree:
            TemplateSet.templates[elem.get("card-type")] = Template(elem)

    @staticmethod
    def get_template(id):
        return TemplateSet.templates[id]

    @staticmethod
    def show_templates():
        for id in TemplateSet.templates:
            TemplateSet.show_template(id)
        
    @staticmethod
    def show_template(id):
        TemplateSet.templates[id].show()
        
