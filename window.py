import curses
import math

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(False)
if curses.has_colors():
    curses.start_color()
stdscr.keypad(True)

curses.init_pair(1,curses.COLOR_RED,curses.COLOR_MAGENTA)

window_config = {"nlines":curses.LINES,"ncols":curses.COLS,"begin_x":0,"begin_y":0,"center":{"x":math.floor(curses.COLS/2.0),"y":math.floor(curses.LINES/2.0)},"caption":"Press a key to quit."}
win = curses.newwin(window_config["nlines"],window_config["ncols"],window_config["begin_x"],window_config["begin_y"])
win.bkgd(' ',curses.color_pair(1))
text = "Window 1"
win.addstr(window_config["center"]["y"], window_config["center"]["x"] - math.floor(len(text)/2),text,curses.color_pair(1) | curses.A_BOLD)
if "" != window_config["caption"]:
    win.addstr(curses.LINES - 2, 0, window_config["caption"],curses.color_pair(1) | curses.A_BOLD)
win.refresh()
# stdscr.addstr(0,0,"Hello, world!")
# screenDetailText = "This screen is [" + str(curses.LINES) + "] high and [" + str(curses.COLS) + "] across."
# startingXPos = int ( (curses.COLS - len(screenDetailText))/2 )
# stdscr.addstr(3, startingXPos, screenDetailText)
# stdscr.addstr(5, curses.COLS - len("Press a key to quit."), "Press a key to quit.")
win.getch()

#stdscr.refresh()
#stdscr.getch()

curses.echo()
curses.nocbreak()
curses.curs_set(True)
stdscr.keypad(False)
curses.endwin()