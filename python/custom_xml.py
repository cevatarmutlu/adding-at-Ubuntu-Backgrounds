import xml.etree.ElementTree as ET
from os import listdir

class CustomXML:
    def __init__(self, xml_path, wallpapers_path):
        self.tree = ET.parse(xml_path)
        self.root = self.tree.getroot()
        self.wallpapers_path = wallpapers_path
        self.wallpapers_list = self.get_wallpapers(self.wallpapers_path)

    def get_wallpapers(self, path):
        return listdir(path)

    def create_sub_element(self, wallpaper, tag_name, tag_text):
        sub = wallpaper.makeelement(tag_name, {})
        sub.text = tag_text
        return sub

    def create_element(self, element, properties_dict, properties_value_dict):
        for key, value in properties_value_dict.items():
            properties_dict[key] = value

        sub_elements = [ self.create_sub_element(element, key, value) for (key, value) in properties_dict.items()]

        [element.append(i) for i in sub_elements]

        return element

    def __str__(self):
        return "{self.tree}, {self.root}, {self.wallpapers_path}, {self.wallpapers_list}".format(self=self)
