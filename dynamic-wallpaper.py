import os
import random

wallpapers_path = "/usr/share/backgrounds/selected/"
wallpapers = os.listdir(wallpapers_path)

wallpaper = random.choice(wallpapers)
wallpaper_path = wallpapers_path + wallpaper 

def change_wallpaper():
    os.system(f'gsettings set org.cinnamon.desktop.background picture-uri "file://{wallpaper_path}"')

change_wallpaper()
