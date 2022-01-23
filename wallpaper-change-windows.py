import ctypes

class Main:
    def __init__(self):
        path = 'c:/...'
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)

application = Main()