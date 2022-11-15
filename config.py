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
        # Check if the file exists
        if path.exists(filename):
            with open(filename,"r") as instream:
                content = instream.readline()
                # Check if the content contains cells, positions of players and obstacles
                pattern = compile(r"^(_+)1(_+)(x*)(_+)2(_+)$")
                if search(pattern,content):
                    return Scene(content)
        else:
            with open(filename,"x") as outstream:
                default_scene = "___1_____x__2___"
                outstream.write(default_scene)
                return Scene(default_scene)

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