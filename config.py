import re
import os
import json
import player
import scene
import exceptions

def load_scene(filename=""):
    """Returns a Scene instance"""
    scene_pattern = "___1_____x__2___"
    # Check if a filename is specified
    if filename != "":
        try:
            # Check if the filename has a valid extension
            pattern = re.compile(r"\.ffscene")
            if re.search(pattern,filename):
                # Check if the file existts
                if os.path.exists(filename):
                    content = ""
                    with open(filename,"r") as instream:
                        content = instream.readline()
                    # Check if the content of the file matches a valid scene pattern
                    pattern = re.compile(r"^(_+)(x|_)*1(x|_)*(_+)(x|_)*2(x|_)*(_+)$")
                    if re.search(pattern,content):
                        scene_pattern = content
                    else:
                        raise exceptions.InvalidPattern("Wrong scene format. Using default value.")
                else:
                    raise exceptions.FileNotExists(f"{filename} does not exist. Using default value")
            else:
                raise exceptions.InvalidPattern("Wrong file extension. Using default value.")
        except (exceptions.InvalidPattern,exceptions.FileNotExists) as e:
            print(e)
    return scene.Scene(scene_pattern)

def load_player(filename):
    """Returns an instance of a player by reading its properties in the dedicated file"""
    p = {"player_type": "NONE","movement_speed":-1,"attacking_range":-1,"defending_range": -1,"blocking_time":-1}
    try:
        # Check if the file has a valid extension
        pattern = re.compile(r"\.ffplayer$")
        if re.search(pattern,filename):
            # Check if the file exists
            if os.path.exists(filename):
                with open(filename,"r") as instream:
                    p = json.load(instream)
            else:
                raise exceptions.FileNotExists(f"{filename} does not exist.\nStopping...")
        else:
            raise exceptions.InvalidPattern("Wrong file format.\nStopping...")
    except (exceptions.InvalidPattern,exceptions.FileNotExists) as e:
        print(e)
    except json.JSONDecodeError:
        print(f"Wrong syntax in {filename}, must be written like JSON.\nStopping...")
    return player.Player(p["player_type"],p["movement_speed"],p["attacking_range"],p["defending_range"],p["blocking_time"])