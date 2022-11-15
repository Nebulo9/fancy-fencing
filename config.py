from re import search,sub,compile,MULTILINE
from os import path
from json import load,JSONDecodeError
from player import Player

# Returns a dictionnary containing the properties of the scene
def load_scene(filename="default.ffscene"):
    # Check if the file has the correct extension
    if search(r"\.ffscene$",filename):
        # Check if the file exists
        if path.exists(filename):
            with open(filename,"r") as instream:
                content = instream.readline()
                # Check if the content contains cells, positions of players and obstacles
                pattern = compile(r"^(_|x)+|1|2$")
                if search(pattern,content):
                    length = len(content)
                    pos_p1 = content.index("1")
                    pos_p2 = content.index("2")
                    pos_obs = [i for i,char in enumerate(content) if char == 'x']
                    # Returning the dictionnary with the properties of the scene
                    return {"length":length, "pos_p1":pos_p1, "pos_p2":pos_p2, "pos_obs":pos_obs}
        else:
            with open(filename,"x") as outstream:
                default_scene = "___1_____x__2___"
                outstream.write(default_scene)
                length = len(default_scene)
                pos_p1 = default_scene.index("1")
                pos_p2 = default_scene.index("2")
                pos_obs = [i for i,char in enumerate(default_scene) if char == 'x']
                return {"length":length, "pos_p1":pos_p1, "pos_p2":pos_p2, "pos_obs":pos_obs}

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