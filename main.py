import sys
import exceptions
import game

if __name__ == "__main__":
    try:
        if len(sys.argv) == 1: raise exceptions.ArgumentsNumber("You must provide a positive integer FPS value.")
        fps = int(sys.argv[1])
        if fps and fps > 0:
            if len(sys.argv) == 3:
                save_filename = sys.argv[2]
                g = game.Game(fps,"./p1.ffplayer","./p2.ffplayer","./default.ffscene",save_filename)
            else:
                g = game.Game(fps,"./p1.ffplayer","./p2.ffplayer","./default.ffscene")
            g.start()
        else:
            raise exceptions.IllegalArgument("You must provide a positive integer FPS value.")
    except (exceptions.IllegalArgument,exceptions.ArgumentsNumber) as e:
        print(e)
        exit()