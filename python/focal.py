from python.custom_xml import CustomXML

class Focal(CustomXML):
    def __init__(self, xml_path, wallpapers_folder_path, wallpapers_currrent_path, static_duration=1795, transition_duration=5):
        super().__init__(xml_path, wallpapers_folder_path, wallpapers_currrent_path)
        self.static_key_value = {
            "duration": str(float(static_duration)),
            "file": ''
        }
        self.transition_key_value = {
            "duration": str(float(transition_duration)),
            "from": '',
            'to': ''
        }

    def changeLastTo(self):
        self.root.findall("transition")[-1].find("to").text = self.wallpapers_list[0]

    def generateFocalTags(self):
        focal_tags = [(self.create_element(self.root.makeelement("static", {}), self.static_key_value, {"file": self.wallpapers_folder_path + "/" + image}), self.create_element(self.root.makeelement("transition", {}), self.transition_key_value, {"from": self.wallpapers_folder_path + "/" + image, "to": self.wallpapers_list[i + 1] if i != len(self.wallpapers_list) - 1 else "/usr/share/backgrounds/Focal-Fossa_WP_4096x2304_GREY.png"})) for i, image in enumerate(self.wallpapers_list)]
        return focal_tags

    def generate(self):

        # focal dosyasındaki son to listemizdeki ilk resim ile değiştirildi
        self.changeLastTo()

        focal_tags = self.generateFocalTags()

        # append tags to root
        [(self.root.append(static), self.root.append(transition)) for static, transition in focal_tags]

        self.tree.write("files/new_focal.xml")

