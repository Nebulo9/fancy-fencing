from re import search,compile
from os import path
from json import load,JSONDecodeError
from player import Player
from scene import Scene
from exceptions import InvalidPattern,FileNotExists

def load_scene(filename=""):
    """Returns a Scene instance"""
    scene = "___1_____x__2___"
    # Check if a filename is specified
    if filename != "":
        try:
            # Check if the filename has a valid extension
            pattern = compile(r"\.ffscene")
            if search(pattern,filename):
                # Check if the file existts
                if path.exists(filename):
                    content = ""
                    with open(filename,"r") as instream:
                        content = instream.readline()
                    # Check if the content of the file matches a valid scene pattern
                    pattern = compile(r"^(_+)(x|_)*1(x|_)*(_+)(x|_)*2(x|_)*(_+)$")
                    if search(pattern,content):
                        scene = content
                    else:
                        raise InvalidPattern("Wrong scene format. Using default value.")
                else:
                    raise FileNotExists(f"{filename} does not exist. Using default value")
            else:
                raise InvalidPattern("Wrong file extension. Using default value.")
        except (InvalidPattern,FileNotExists) as e:
            print(e)
    return Scene(scene)

def load_player(filename: str):
    """Returns an instance of a player by reading its properties in the dedicated file"""
    p = {"player_type": "NONE","movement_speed":-1,"attacking_range":-1,"defending_range": -1,"blocking_time":-1}
    try:
        # Check if the file has a valid extension
        pattern = compile(r"\.ffplayer$")
        if search(pattern,filename):
            # Check if the file exists
            if path.exists(filename):
                with open(filename,"r") as instream:
                    p = load(instream)
            else:
                raise FileNotExists(f"{filename} does not exist.\nStopping...")
        else:
            raise InvalidPattern("Wrong file format.\nStopping...")
    except (InvalidPattern,FileNotExists) as e:
        print(e)
    except JSONDecodeError:
        print(f"Wrong syntax in {filename}, must be written like JSON.\nStopping...")
    return Player(p["player_type"],p["movement_speed"],p["attacking_range"],p["defending_range"],p["blocking_time"])