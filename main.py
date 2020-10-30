from os import getcwd
from python.focal import Focal
from python.focal_wallpapers import FocalWallpaper

if __name__ == "__main__":

    wallpapers_folder_path = "/home/cevat/Pictures/wallpapers"
    wallpapers_currrent_path = '/home/cevat/Downloads/at'
    
    focal_path = getcwd() + "/files/focal.xml"
    focal_wallpaper_path = getcwd() + "/files/focal-wallpapers.xml"

    FocalWallpaper(focal_wallpaper_path, wallpapers_folder_path, wallpapers_currrent_path).generate()
    Focal(focal_path, wallpapers_folder_path, wallpapers_currrent_path).generate()