import config
import game

scene_config = config.load_scene()
player1_config = config.load_player("./p1.ffplayer")

game.start_game(scene_config, player1_config, player1_config)