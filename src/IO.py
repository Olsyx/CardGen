import math
import xml.etree.ElementTree as ET
import io
import os

class IO:
    files = {}

    @staticmethod
    def open_file(name, path, mode):
        IO.files[name] = open(path, mode, encoding="utf-8")
        
    @staticmethod
    def clone_file(path, new_path):
        origin = open(path, "r", encoding="utf-8")
        dest = open(new_path, "w", encoding="utf-8")
        dest.write(origin.read())
        origin.close()
        dest.close()
    
    @staticmethod
    def write_to(name, text):
        IO.files[name].write(text)
        
    @staticmethod
    def read(name):
        return IO.files[name].read()
        
    @staticmethod
    def end(name):
        IO.files[name].close()
        del IO.files[name]
        
    @staticmethod
    def read_xml(name, path):
        if path is None:
            return None

        IO.open_file(name, path, "r")
        text = IO.read(name)
        return ET.fromstring(text)