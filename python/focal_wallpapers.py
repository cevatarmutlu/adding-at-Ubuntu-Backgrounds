from python.custom_xml import CustomXML

class FocalWallpaper(CustomXML):
    def __init__(self, xml_path, wallpapers_folder_path, wallpapers_currrent_path):
        super().__init__(xml_path, wallpapers_folder_path, wallpapers_currrent_path)
        self.wallpapers_tag = {
            "name": "",
            'filename': "",
            'options': "zoom",
            "pcolor": "#000000",
            "scolor": "#000000",
            "shade_type": "solid"
        }

    def generateWallpapersTags(self):
        wallpapers_tags = [self.create_element(self.root.makeelement("wallpaper", {}), self.wallpapers_tag, {"name":i.split(".")[0], "filename": self.wallpapers_folder_path + "/" + i}) for i in self.wallpapers_list]
        return wallpapers_tags

    def generate(self):
     
        wallpapers_tags = self.generateWallpapersTags()

        [self.root.append(i) for i in wallpapers_tags]

        self.tree.write("files/new_focal-wallpapers.xml")