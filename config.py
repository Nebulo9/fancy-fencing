import re
import os
import json
import player
import scene
import exceptions
import time

def load_scene(filename=""):
    """Returns a Scene instance."""
    scene_pattern = "___1_____x__2___"
    # Check if a filename is specified
    if filename != "":
        try:
            # Check if the filename has a valid extension
            pattern = re.compile(r"\.ffscene")
            if not re.search(pattern,filename): raise exceptions.InvalidPattern("Wrong file format.\nStopping...")
            if not os.path.exists(filename): raise exceptions.FileNotExists(f"{filename} does not exist.\nStopping...")
            content = ""
            with open(filename,"r") as instream:
                content = instream.readline()
            # Check if the content of the file matches a valid scene pattern
            pattern = re.compile(r"^(_+)(x|_)*1(x|_)*(_+)(x|_)*2(x|_)*(_+)$")
            if not re.search(pattern,content): raise exceptions.InvalidPattern("Wrong scene format. Using default value.")
            scene_pattern = content
        except (exceptions.InvalidPattern,exceptions.FileNotExists) as e:
            print(e)
    return scene.Scene(scene_pattern)

def load_player(filename):
    """Returns an instance of a player by reading its properties in the dedicated file."""
    p = {"player_type": "NONE","movement_speed":-1,"attacking_range":-1,"defending_range": -1,"blocking_time":-1}
    try:
        # Check if the file has a valid extension
        pattern = re.compile(r"\.ffplayer$")
        if not re.search(pattern,filename): raise exceptions.InvalidPattern("Wrong file format.\nStopping...")
        if not os.path.exists(filename): raise exceptions.FileNotExists(f"{filename} does not exist.\nStopping...")
        with open(filename,"r") as instream:
            p = json.load(instream)
    except (exceptions.InvalidPattern,exceptions.FileNotExists) as e:
        print(e)
    except json.JSONDecodeError:
        print(f"Wrong syntax in {filename}, must be written like JSON.\nStopping...")
    return player.Player(p["player_type"],p["movement_speed"],p["attacking_range"],p["defending_range"],p["blocking_time"])

def load_save(filename):
    try:
        pattern = re.compile(r'\.ffsave$')
        if not re.search(pattern,filename): raise exceptions.InvalidPattern("Wrong file format.\nStopping...")
        if not os.path.exists(filename): raise exceptions.FileNotExists(f"{filename} does not exist.\nStopping...")
        conf = {}
        with open(filename,"r") as instream:
            conf = json.load(instream)
        return conf
    except (exceptions.InvalidPattern,exceptions.FileNotExists) as e:
        print(e)
    except json.JSONDecodeError:
        print(f"Wrong syntax in {filename}, must be written like JSON.\nLoading a new game...")

def save(conf):
    filename = "save_" + time.strftime("%d-%m-%y_%H-%M-%S",time.localtime()) + ".ffsave"
    with open(filename,"x") as outstream:
        outstream.write(json.dumps(conf))