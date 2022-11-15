import window
import curses

class Game:
    def __init__(self,scene,player1,player2):
        self.__scene = scene
        self.__player1 = player1
        self.__player2 = player2
    
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
