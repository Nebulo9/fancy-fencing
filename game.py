import window
import curses

def start_game(scene,player1,player2):
    window.start_session()
    pairs = [{"number": 1,"fg":curses.COLOR_WHITE,"bg":curses.COLOR_BLACK}]
    game_win = window.create_window(pairs)
    
    while True:
        c = game_win.getch()
        if c == ord('q'):
            move_left(player1)
        elif c == curses.KEY_LEFT:
            move_left(player2)
        elif c == ord('d'):
            move_right(player1)
        elif c == curses.KEY_RIGHT:
            move_right(player2)
        elif c == ord('a'):
            jump_left(player1)
        elif c == ord('l'):
            jump_left(player2)
        elif c == ord('e'):
            jump_right(player1)
        elif c == ord('m'):
            jump_right(player2)
        elif c == ord('z'):
            make_attack(player1)
        elif c == ord('o'):
            make_attack(player2)
        elif c == curses.KEY_ENTER:
            window.end_session()
            break
    end_game()

def end_game(scores=0):
    return True

def move_right(player):
    return True

def move_left(player):
    return True

def jump_left(player):
    return True

def jump_right(player):
    return True

def make_attack(player):
    return True