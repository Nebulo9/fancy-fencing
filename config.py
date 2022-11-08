from re import search
from re import MULTILINE
from re import sub
from os import path
from os import getcwd

# Returns a dictionnary containing the properties of the scene
def load_scene(filename="default.ffscene"):
    # Check if the file exists
    if path.exists(filename):
        # Check if the file has the correct extension
        if search(r"\.ffscene$",filename):
            with open(filename,"r") as instream:
                content = instream.readline()
                # Check if the content contains cells, positions of players and obstacles
                if search(r"^(_|x)+|(1{1})|(2{1})$",content):
                    length = len(content)
                    pos_p1 = content.index("1")
                    pos_p2 = content.index("2")
                    pos_obs = [i for i,char in enumerate(content) if char == 'x']
                    # Returning the dictionnary with the properties of the scene
                    return {"length":length, "pos_p1":pos_p1, "pos_p2":pos_p2, "pos_obs":pos_obs}

# Returns a dictionnary containing the attributes of a player
def load_player(filename):
    # Check if the file exists
    if path.exists(filename):
        # Check if the file has the correct extension
        if search(r"\.ffplayer$",filename):
            with open(filename,"r") as instream:
                content = instream.readline()
                # Removing spaces, brackets, quotes from the content and splitting it to have lists containing a property and its value
                splitted = [s.split(":") for s in sub(r"{|}|\s|\"","",content).split(",")]
                player = {}
                # Mapping the properties and their values into a dictionnary
                for l in splitted:
                    player[l[0]] = float(l[1])
                player["player"] = int(player["player"])
                return player