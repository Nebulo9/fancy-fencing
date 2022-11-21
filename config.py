from re import search,compile
from os import path
from json import load,JSONDecodeError
from player import Player
from scene import Scene

# Returns a dictionnary containing the properties of the scene
def load_scene(filename="default.ffscene"):
    # Check if the file has the correct extension
    pattern = compile(r"\.ffscene$")
    if search(pattern,filename):
        scene = "___1_____x__2___"
        # If the file exists, we read its contents
        # Otherwise we use the default scene
        if path.exists(filename):
            content = ""
            with open(filename,"r") as instream:
                content = instream.readline()
            try:
                # We check if the scene has a valid pattern
                pattern = compile(r"^(_+)1(_+)(x*)(_+)2(_+)$")
                if not search(pattern,content):
                    raise Exception
                else:
                    scene = content
            except Exception:
                print("Wrong scene format. Using default value.")
        return Scene(scene)

# Returns a dictionnary containing the attributes of a player
def load_player(filename):
    # Check if the file has the correct extension
    if search(r"\.ffplayer$",filename):
        # Check if the file exists
        if path.exists(filename):
            with open(filename,"r") as instream:
                # Returns a dict containing the player configuration
                try:
                    p = load(instream)
                    return Player(p["player_type"],p["movement_speed"],p["attacking_range"],p["defending_range"],p["blocking_time"])
                except JSONDecodeError:
                    print(f"Wrong syntax in {filename}, must be written like JSON")
                    exit()