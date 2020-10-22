from focal_wallapapers import focal_wallpapers
from focal import focal
from os import getcwd

if __name__ == "__main__":

    wallpaper_path = "/home/cevat/Pictures/wallpapers"
    
    
    focal_path = getcwd() + "/files/focal.xml"
    focal_wallpaper_path = getcwd() + "/files/focal-wallpapers.xml"

    focal_wallpapers(wallpaper_path, focal_wallpaper_path)
    focal(wallpaper_path, focal_path)