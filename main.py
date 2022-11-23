from sys import argv
from exceptions import IllegalArgument,ArgumentsNumber
from game import Game

if __name__ == "__main__":
    try:
        if len(argv) == 1: raise ArgumentsNumber("You must provide a positive integer FPS value.")
        fps = int(argv[1])
        if fps and fps > 0:
            g = Game(fps,"./p1.ffplayer","./p2.ffplayer","./default.ffscene")
            g.start()
        else:
            raise IllegalArgument("You must provide a positive integer FPS value.")
    except (IllegalArgument,ArgumentsNumber) as e:
        print(e)
        exit()