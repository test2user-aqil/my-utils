import os
import random
import time

wallpapers_path = "/usr/share/backgrounds/selected/"
wallpapers = os.listdir(wallpapers_path)


def change_wallpaper():
    wallpaper = random.choice(wallpapers)
    wallpaper_path = wallpapers_path + wallpaper
    os.system(
        f'gsettings set org.cinnamon.desktop.background picture-uri "file://{wallpaper_path}"'
    )
    print(">>>")


while True:
    time.sleep(60 * 10)  # Run every 10 minutes
    change_wallpaper()
