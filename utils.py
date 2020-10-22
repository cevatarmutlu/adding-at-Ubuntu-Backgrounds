from os import listdir
import xml.etree.ElementTree as ET
from xml.dom import minidom

def get_wallpapers(path):
    return listdir(path)

def get_RootAndTree(xml_path):
    tree = ET.parse(xml_path)
    return tree.getroot(), tree


def create_sub_element(wallpaper, tag_name, tag_text):
    sub = wallpaper.makeelement(tag_name, {})
    sub.text = tag_text
    return sub

def create_element(element, properties_dict, properties_value_dict):
    for key, value in properties_value_dict.items():
        properties_dict[key] = value

    sub_elements = [ create_sub_element(element, key, value) for (key, value) in properties_dict.items()]

    [element.append(i) for i in sub_elements]

    return element