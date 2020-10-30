from os import getcwd
from python.focal import Focal
from python.focal_wallpapers import FocalWallpaper
import subprocess
from os import system

if __name__ == "__main__":

    wallpapers_folder_path = "/home/cevat/Pictures/wallpapers"
    wallpapers_currrent_path = ''

    system('chmod +x ' + getcwd() + '/bash/*.sh')
    system(getcwd() + "/bash/copyXML.sh")
    system(getcwd() + "/bash/copyWallpapers.sh " + wallpapers_currrent_path + " " + wallpapers_folder_path)


    focal_path = getcwd() + "/files/focal.xml"
    focal_wallpaper_path = getcwd() + "/files/focal-wallpapers.xml"

    FocalWallpaper(focal_wallpaper_path, wallpapers_folder_path, wallpapers_currrent_path).generate()
    Focal(focal_path, wallpapers_folder_path, wallpapers_currrent_path).generate()

    system(getcwd() + "/bash/move.sh " + wallpapers_currrent_path)