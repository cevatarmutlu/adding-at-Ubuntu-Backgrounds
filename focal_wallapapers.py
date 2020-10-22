import utils

def focal_wallpapers(wallpapers_path, focal_wallpapers_path):
    wallpapers_list = utils.get_wallpapers(wallpapers_path)

    root, tree = utils.get_RootAndTree(focal_wallpapers_path)
    
    wallpapers_tag = {
        "name": "",
        'filename': "",
        'options': "zoom",
        "pcolor": "#000000",
        "scolor": "#000000",
        "shade_type": "solid"
    }
    wallpapers_tags = [utils.create_element(root.makeelement("wallpaper", {}), wallpapers_tag, {"name":i.split(".")[0], "filename": wallpapers_path + "/" + i}) for i in wallpapers_list]

    [root.append(i) for i in wallpapers_tags]

    tree.write("files/new_focal-wallpapers.xml")