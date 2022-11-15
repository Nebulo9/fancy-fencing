import curses
import math
from copy import deepcopy

class GWin:
    # __stdscr = curses.initscr()
    def __init__(self,__color_pairs):
        self.__color_pairs = __color_pairs
    
    def create(self):
        self.__start_session()
        for pair in self.color_pairs:
            curses.init_pair(pair["number"],pair["fg"],pair["bg"])
        self.__conf = {"height": curses.LINES,"width": curses.COLS,"center":(math.floor(curses.COLS/2.0),math.floor(curses.LINES/2.0)),"caption": "Fency Fencing"}
        self.__win = curses.newwin(self.conf["height"],self.conf["width"],0,0)
        self.update_window(self.conf["caption"],x=(self.conf["center"][0] - math.floor(len(self.conf["caption"])/2.0)),attributes=(curses.color_pair(1) | curses.A_BOLD))

    def update_window(self,__str,x=0,y=0,attributes=[]):
        if attributes:
            self.win.addstr(y,x,__str,attributes)
        else:
            self.win.addstr(y,x,__str)
        self.win.refresh()
    
    def __start_session(self):
        curses.noecho()
        curses.cbreak()
        curses.curs_set(False)
        if curses.has_colors():
            curses.start_color()
        GWin.__stdscr.keypad(True)
    
    def end(self):
        curses.echo()
        curses.nocbreak()
        curses.curs_set(True)
        GWin.__stdscr.keypad(False)
        curses.endwin()
    
    @property
    def color_pairs(self):
        return deepcopy(self.__color_pairs)
    @property
    def conf(self):
        return copy(self.__conf)
    @property
    def win(self):
        return self.__win