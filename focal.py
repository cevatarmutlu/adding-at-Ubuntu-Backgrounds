import utils

def focal(wallpapers_path, focal_path):

    root, tree = utils.get_RootAndTree(focal_path)

    wallpapers_list = utils.get_wallpapers(wallpapers_path)
    root.findall("transition")[-1].find("to").text = wallpapers_list[0]

    static_key_value = {
        "duration": "1795.0",
        "file": ''
    }

    transition_key_value = {
        "duration": "5.0",
        "from": '',
        'to': ''
    }

    focal_tags = [(utils.create_element(root.makeelement("static", {}), static_key_value, {"file": wallpapers_path + "/" + image}), utils.create_element(root.makeelement("transition", {}), transition_key_value, {"from": wallpapers_path + "/" + image, "to": wallpapers_list[i + 1] if i != len(wallpapers_list) - 1 else "/usr/share/backgrounds/Focal-Fossa_WP_4096x2304_GREY.png"})) for i, image in enumerate(wallpapers_list)]


    [(root.append(static), root.append(transition)) for static, transition in focal_tags]

    tree.write("files/new_focal.xml")