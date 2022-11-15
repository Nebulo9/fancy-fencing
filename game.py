import window
import curses
import config

class Game:
    def __init__(self,player1_file,player2_file="",scene_file="default.ffscene",fps=60):
        self.__scene = config.load_scene(scene_file)
        self.__player1 = config.load_player(player1_file)
        if player2_file != "":
            self.__player2 = config.load_player(player2_file)
        else:
            self.__player2 = {}
    
    def start(self):
        pairs = [{"number": 1,"fg":curses.COLOR_WHITE,"bg":curses.COLOR_BLACK}]
        self.__win = window.GWin(pairs)
        self.__win.create()
    
    def end(self):
        return True

    @property
    def scene(self):
        return self.__scene
    @property
    def player1(self):
        return self.__player1
    @property
    def player2(self):
        return self.__player2
