import ctypes

class wallpaperchange:
    def __init__(self, path, changevar):
        
        self.path = path
        self.changevar=changevar
        def changewall(self):
            ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)

path="G:\\Library\\Documents\\VScode\\esp32-wallpaper-led-alexa\\2.jpg"


