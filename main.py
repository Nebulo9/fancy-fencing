from sys import argv
try:
    if len(argv) == 1: raise Exception
    fps = int(argv[1])
    if fps and fps > 0:
        print(argv)
        # g = Game("./p1.ffplayer",argv[0])
    else:
        raise Exception
except Exception:
    print("You must provide a positive integer FPS value.")