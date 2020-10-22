from os import getcwd
from python.focal import Focal
from python.focal_wallpapers import FocalWallpaper

if __name__ == "__main__":

    wallpaper_path = "/home/cevat/Pictures/wallpapers"
    
    
    focal_path = getcwd() + "/files/focal.xml"
    focal_wallpaper_path = getcwd() + "/files/focal-wallpapers.xml"

    FocalWallpaper(focal_wallpaper_path, wallpaper_path).generate()
    Focal(focal_path, wallpaper_path).generate()