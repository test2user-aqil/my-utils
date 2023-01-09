import os
import time

wallpapers_path = "/usr/share/backgrounds/selected/"
wallpapers = os.listdir(wallpapers_path)
count = len(wallpapers)


def change_wallpaper(path):
    os.system(
        f'gsettings set org.cinnamon.desktop.background picture-uri "file://{path}"'
    )


i = 0
while True:
    time.sleep(60 * 10)  # Run every 10 minutes
    change_wallpaper(wallpapers_path + wallpapers[i])

    i += 1
    if i == count:
        i = 0
