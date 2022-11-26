import time
import window
import curses
import config
import threading

class Game:
    def __init__(self,fps,player1_file,player2_file="",scene_file=""):
        self.__scene = config.load_scene(scene_file)
        self.__player1 = config.load_player(player1_file)
        self.__player2 = config.load_player(player2_file)
        self.__fps = 1/fps
    
    def start(self):
        pairs = [{"number": 1,"fg":curses.COLOR_WHITE,"bg":curses.COLOR_BLACK}]
        self.__win = window.GWin(pairs)
        self.win.create()
        self.scene_start = (self.win.conf["center"][0]-(self.scene.length//2))
        self.scene_end = self.scene_start+self.scene.length
        self.obs = [i+self.scene_start for i in self.scene.pos_obs]
        try:
            self._diplay_start(self.scene_start)
            while True:
                # Obstacles
                for i in self.obs:
                    self.win.update_window("x",i,curses.LINES-2)
                key = self.win.win.getch()
                if chr(key) == 'g':
                    break
                else:
                    t1 = threading.Thread(target=self._action,args=(self.player1,key))
                    t2 = threading.Thread(target=self._action,args=(self.player2,key))
                    t1.start()
                    t2.start()
                    t1.join()
                    t2.join()
        except Exception as e:
            self.end()
            print(e)
            exit()
        self.end()
    
    def end(self):
        self.win.end()

    def _display_player(self,player):
        base_y = curses.LINES-2
        self.win.update_window(player.body.foot.part,player.body.foot.pos[0],y=base_y-player.body.foot.pos[1])
        self.win.update_window(player.body.midlow.part,player.body.midlow.pos[0],y=base_y-player.body.midlow.pos[1])
        self.win.update_window(player.body.midtop.part,player.body.midtop.pos[0],y=base_y-player.body.midtop.pos[1])
        self.win.update_window(player.body.head.part,player.body.head.pos[0],y=base_y-player.body.head.pos[1])

    def _display_clear(self,player):
        base_y = curses.LINES-2
        self.win.update_window(" " * player.body.foot.length,player.body.foot.pos[0],y=base_y-player.body.foot.pos[1])
        self.win.update_window(" " * player.body.midlow.length,player.body.midlow.pos[0],y=base_y-player.body.midlow.pos[1])
        self.win.update_window(" " * player.body.midtop.length,player.body.midtop.pos[0],y=base_y-player.body.midtop.pos[1])
        self.win.update_window(" " * player.body.head.length,player.body.head.pos[0],y=base_y-player.body.head.pos[1])
    
    def _diplay_start(self,start_pos_scene):
        # Scene
        self.win.update_window("=" * (self.scene.length),x=start_pos_scene,y=curses.LINES-1)
        
        # Player 1
        self.player1.pos = (start_pos_scene + self.scene.pos_p1,0)
        self._display_player(self.player1)

        # Player 2
        self.player2.pos = (start_pos_scene + self.scene.pos_p2,0)
        self._display_player(self.player2)
        
        # Obstacles
        for i in self.obs:
            self.win.update_window("x",i,curses.LINES-2)
    
    def _action(self,player,key):
        if player.player_type == "1":
            if chr(key) == 'd':
                if not self._is_there_player(player,self.player2,1) and not self._is_there_obstacle(player,1):
                    self._move_right(player)
            elif chr(key) == 'q':
                if not self._is_there_player(player,self.player2,-1) and not self._is_there_obstacle(player,-1):
                    self._move_left(player)
            elif chr(key) == 'z':
                self._change_state(player,"attacking")
            elif chr(key) == 's':
                self._change_state(player,"blocking")
            elif chr(key) == 'e':
                if not self._is_there_player(player,self.player2,1):
                    self._jump_right(player)
            elif chr(key) == 'a':
                if not self._is_there_player(player,self.player2,1):
                    self._jump_left(player)
        else:
            if key == curses.KEY_RIGHT:
                if not self._is_there_player(player,self.player1,1) and not self._is_there_obstacle(player,1):
                    self._move_right(player)
            elif key == curses.KEY_LEFT:
                if not self._is_there_player(player,self.player1,-1) and not self._is_there_obstacle(player,-1):
                    self._move_left(player)
            elif chr(key) == 'o':
                self._change_state(player,"attacking")
            elif chr(key) == 'p':
                self._change_state(player,"blocking")
            elif chr(key) == 'm':
                if not self._is_there_player(player,self.player2,1):
                    self._jump_right(player)
            elif chr(key) == 'l':
                if not self._is_there_player(player,self.player2,1):
                    self._jump_left(player)
        
    def _is_there_obstacle(self,player,direction):
        if player.player_type == "1":
            if direction > 0:
                return (player.pos[0] + 1 in self.obs) or (player.pos[0] + 1 == self.scene_end)
            return (player.body.foot.pos[0] - 1 in self.obs) or (player.body.foot.pos[0] - 1 == self.scene_start)
        else:
            if direction > 0:
                return ((player.body.foot.pos[0] + player.body.foot.length) in self.obs) or (player.body.foot.pos[0] + player.body.foot.length) == self.scene_end
            return (player.pos[0] - 1 in self.obs) or (player.pos[0] - 1 == self.scene_start)

    def _is_there_player(self,player,target,direction):
        if direction > 0:
            return ((player.body.head.pos[0] + player.body.head.length) == target.body.head.pos[0])
        return (player.body.head.pos[0] == (target.body.head.pos[0] + target.body.head.length))
            
    def _move_right(self,player):
        time.sleep(self.fps*player.movement_speed)
        self._display_clear(player)
        player.pos = (player.pos[0]+1,player.pos[1])
        self._display_player(player)

    def _move_left(self,player):
        time.sleep(self.fps*player.movement_speed)
        self._display_clear(player)
        player.pos = (player.pos[0]-1,player.pos[1])
        self._display_player(player)
    
    def _jump_right(self,player):
        # Up
        time.sleep(self.fps*player.movement_speed)
        self._display_clear(player)
        player.pos = (player.pos[0],player.pos[1]+1)
        self._display_player(player)
        # Right 1
        time.sleep(self.fps*(player.movement_speed/3))
        self._display_clear(player)
        player.pos = (player.pos[0]+1,player.pos[1])
        self._display_player(player)
        # Right 2
        time.sleep(self.fps*(player.movement_speed/3))
        self._display_clear(player)
        player.pos = (player.pos[0]+1,player.pos[1])
        self._display_player(player)
        # Right 3
        time.sleep(self.fps*(player.movement_speed/3))
        self._display_clear(player)
        player.pos = (player.pos[0]+1,player.pos[1])
        self._display_player(player)
        # Down
        time.sleep(self.fps*player.movement_speed)
        self._display_clear(player)
        player.pos = (player.pos[0],player.pos[1]-1)
        self._display_player(player)

    def _jump_left(self,player):
        # Up
        time.sleep(self.fps*player.movement_speed)
        self._display_clear(player)
        player.pos = (player.pos[0],player.pos[1]+1)
        self._display_player(player)
        # Left 1
        time.sleep(self.fps*(player.movement_speed/3))
        self._display_clear(player)
        player.pos = (player.pos[0]-1,player.pos[1])
        self._display_player(player)
        # Left 2
        time.sleep(self.fps*(player.movement_speed/3))
        self._display_clear(player)
        player.pos = (player.pos[0]-1,player.pos[1])
        self._display_player(player)
        # Left 3
        time.sleep(self.fps*(player.movement_speed/3))
        self._display_clear(player)
        player.pos = (player.pos[0]-1,player.pos[1])
        self._display_player(player)
        # Down
        time.sleep(self.fps*player.movement_speed)
        self._display_clear(player)
        player.pos = (player.pos[0],player.pos[1]-1)
        self._display_player(player)

    def _change_state(self, player,state):
        time.sleep(self.fps)
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
    def scene_start(self):
        return self.__scene_start
    @scene_start.setter
    def scene_start(self,scene_start):
        self.__scene_start = scene_start
    @property
    def fps(self):
        return self.__fps
    @property
    def scene_end(self):
        return self.__scene_end
    @scene_end.setter
    def scene_end(self,scene_end):
        self.__scene_end = scene_end
    @property
    def obs(self):
        return self.__obs
    @obs.setter
    def obs(self,obs):
        self.__obs = obs