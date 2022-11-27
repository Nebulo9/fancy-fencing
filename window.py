import curses

class GWin:
    def __init__(self,__color_pairs):
        self.__color_pairs = __color_pairs
        self.__win = curses.initscr()
    
    def create(self):
        self.__start_session()
        for pair in self.color_pairs:
            curses.init_pair(pair["number"],pair["fg"],pair["bg"])
        self.__conf = {"height": curses.LINES,"width": curses.COLS,"center":(curses.COLS//2,curses.LINES//2),"caption": "Fency Fencing"}
        self.update_window(self.conf["caption"],x=(self.conf["center"][0] - len(self.conf["caption"])//2),attributes=(curses.color_pair(1) | curses.A_BOLD))

    def update_window(self,__str,x=0,y=0,attributes=0):
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
        self.__win.keypad(True)
    
    def end(self):
        curses.echo()
        curses.nocbreak()
        curses.curs_set(True)
        self.__win.keypad(False)
        curses.endwin()
    
    @property
    def color_pairs(self):
        return self.__color_pairs
    @property
    def conf(self):
        return self.__conf
    @property
    def win(self):
        return self.__win