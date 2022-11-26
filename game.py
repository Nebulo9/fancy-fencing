import window
import curses
import config
from threading import Thread

class Game:
    def __init__(self,fps: int,player1_file: str,player2_file="",scene_file=""):
        self.__scene = config.load_scene(scene_file)
        self.__player1 = config.load_player(player1_file)
        self.__player2 = config.load_player(player2_file)
    
    def start(self):
        pairs = [{"number": 1,"fg":curses.COLOR_WHITE,"bg":curses.COLOR_BLACK}]
        self.__win = window.GWin(pairs)
        self.win.create()
        start_pos_scene = (self.win.conf["center"][0]-(self.scene.length//2))
        end_pos_scene = start_pos_scene+self.scene.length
        # Ground/Scene
        try:
            self._diplay_start(start_pos_scene)
            self.__obs = [i+start_pos_scene for i in self.scene.pos_obs]
            while True:
                pos_p1 = self.player1.pos
                pos_p2 = self.player2.pos
                c = self.win.win.getch()
                if chr(c) == 'd':
                    if (pos_p1+3 < pos_p2-2) and (pos_p1+1 not in obs):
                        self._move_right(self.player1)
                elif chr(c) == 'q':
                    if (pos_p1-2 > start_pos_scene-1) and (pos_p1-2 not in obs):
                        self._move_left(self.player1)
                elif chr(c) == 'z':
                    self._change_state(self.player1,"attacking")
                elif chr(c) == 'c':
                    self._change_state(self.player1,"blocking")
                elif c == curses.KEY_RIGHT:
                    if (pos_p2+2 < end_pos_scene) and (pos_p2+2 not in obs):
                        self._move_right(self.player2)
                elif c == curses.KEY_LEFT:
                    if (pos_p2-3 > pos_p1 + 2) and (pos_p2-1 not in obs):
                        self._move_left(self.player2)
                elif chr(c) == 'o':
                    self._change_state(self.player2,"attacking")
                elif chr(c) == 'p':
                    self._change_state(self.player2,"blocking")
                elif chr(c) == 'g':
                    break
        except Exception as e:
            self.end()
            print(e)
            exit()
        self.end()
    
    def end(self):
        self.win.end()

    def _display_player(self,player):
        self.win.update_window(player.body.foot.part,player.body.foot.pos,y=curses.LINES-2)
        self.win.update_window(player.body.midlow.part,player.body.midlow.pos,y=curses.LINES-3)
        self.win.update_window(player.body.midtop.part,player.body.midtop.pos,y=curses.LINES-4)
        self.win.update_window(player.body.head.part,player.body.head.pos,y=curses.LINES-5)

    def _display_clear(self,player):
        self.win.update_window(" " * player.body.foot.length,player.body.foot.pos,y=curses.LINES-2)
        self.win.update_window(" " * player.body.midlow.length,player.body.midlow.pos,y=curses.LINES-3)
        self.win.update_window(" " * player.body.midtop.length,player.body.midtop.pos,y=curses.LINES-4)
        self.win.update_window(" " * player.body.head.length,player.body.head.pos,y=curses.LINES-5)
    
    def _diplay_start(self,start_pos_scene):
        # Scene
        self.win.update_window("=" * (self.scene.length),x=start_pos_scene,y=curses.LINES-1)
        
        # Player 1
        self.player1.pos = start_pos_scene + self.scene.pos_p1
        self._display_player(self.player1)

        # Player 2
        self.player2.pos = start_pos_scene + self.scene.pos_p2
        self._display_player(self.player2)
        
        # Obstacles
        for i in self.scene.pos_obs:
            self.win.update_window("x",start_pos_scene + i,curses.LINES-2)
    
    def _action(self,player,key: int,scene_bounds: tuple[int,int]):
        if player.player_type == "1":
            pos_p = player.pos
            pos_p2 = self.player2.pos
            if chr(key) == 'd':
                if (pos_p + 3 < pos_p2 - 2) and (pos_p + 1 not in self.obs):
                    self._move_right(player)
            elif chr(key) == 'a':
                if (pos_p -2 > )
        else:
        
            
    def _move_right(self,player): 
        self._display_clear(player)
        player.pos += 1
        self._display_player(player)

    def _move_left(self,player):
        self._display_clear(player)
        player.pos -= 1
        self._display_player(player)
    
    def _change_state(self, player,state: str):
        player.state = state
        self._display_player(player)

    @property
    def scene(self):
        return self.__scene
    @property
    def player1(self):
        return self.__player1
    @property
    def player2(self):
        return self.__player2
    @property
    def win(self):
        return self.__win
    @property
    def obs(self):
        return self.__obs