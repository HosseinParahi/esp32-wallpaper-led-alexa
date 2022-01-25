import ctypes
WALLPAPER_PATH = "G:\\Library\\Documents\\VScode\\esp32-wallpaper-led-alexa\\2.jpg"
ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, 3)