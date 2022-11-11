import curses
import math

def start_session():
    curses.noecho()
    curses.cbreak()
    curses.curs_set(False)
    if curses.has_colors():
        curses.start_color()
    stdscr.keypad(True)

def create_window(color_pairs,width=0,height=0):
    for pair in color_pairs:
        curses.init_pair(pair["number"],pair["fg"],pair["bg"])
    window_config = {}
    if width < 1 and height < 1:
        window_config = {"height":curses.LINES,"width":curses.COLS,"center":{"x":math.floor(curses.COLS/2.0),"y":math.floor(curses.LINES/2.0)},"caption":"Fency Fencing"}
    else:
        window_config = {"height":height,"height":width,"center":{"x":math.floor(width/2.0),"y":math.floor(height/2.0)},"caption":"Fency Fencing"}
    win = curses.newwin(window_config["height"],window_config["width"],0,0)
    win.addstr(0, window_config["center"]["x"] - math.floor(len(window_config["caption"])/2),window_config["caption"],curses.color_pair(1) | curses.A_BOLD)
    win.refresh()
    return win

def update_window(x,y,str,win):
    win.addstr(y,x,str)

def end_session():
    curses.echo()
    curses.nocbreak()
    curses.curs_set(True)
    stdscr.keypad(False)
    curses.endwin()

stdscr = curses.initscr()