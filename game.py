import time
import window
import curses
import config
import threading

class Game:
    def __init__(self,fps,player1_file,player2_file,scene_file="",save_file=""):
        self.__scene = config.load_scene(scene_file)
        self.__player1 = config.load_player(player1_file)
        self.__player2 = config.load_player(player2_file)
        self.__fps = 1/fps
        self.__actions = []
        if save_file != "":
            self.__loaded_from_save = True
            self.__saved_conf = config.load_save(save_file)
        self.__pause_elts = {"pause_text":"PAUSE","pause_cmds":"B: Resume - G: Quit - J: Save","p1_cmds":("Player 1","Q/D: Move left/right","A/E: Jump right/left","Z/S: Attack/Block"),"p2_cmds":("Player 2","LEFT_A/RIGHT_A: Move left/right","L/M: Jump right/left","O/P: Attack/Block")}
    
    def start(self):
        pairs = ({"number": 1,"fg":curses.COLOR_WHITE,"bg":curses.COLOR_BLACK},{"number":2,"fg":curses.COLOR_RED,"bg":curses.COLOR_BLACK},{"number":3,"fg":curses.COLOR_GREEN,"bg":curses.COLOR_BLACK})
        self.__win = window.GWin(pairs)
        self.win.create()
        self.scene_start = (self.win.conf["center"][0]-(self.scene.length//2))
        self.scene_end = self.scene_start+self.scene.length
        self.obs = tuple([i+self.scene_start for i in self.scene.pos_obs])
        try:
            self._diplay_start(self.scene_start)
            self.paused = False
            while True:
                # Obstacles
                for i in self.obs:
                    self.win.update_window("x",i,curses.LINES-2)
                t3 = threading.Thread(target=self._buffer_actions)
                t3.start()
                key = self.win.win.getch()
                t1 = threading.Thread(target=self._action,args=(self.player1,key))
                t2 = threading.Thread(target=self._action,args=(self.player2,key))
                if chr(key) == 'g' and self.paused:
                    break
                elif chr(key) == 'b':
                    if self.paused:
                        self.paused = False
                        self._clear_pause()
                    else:
                        self.paused = True
                        self._display_pause()
                elif chr(key) == 'j' and self.paused:
                    self._save()
                elif not self.paused:
                    t1.start()
                    t2.start()
                    t1.join()
                    t2.join()
                    t3.join()
        except Exception as e:
            self.end()
            print(e)
            exit()
        self.end()
    
    def end(self):
        self.win.end()

    def _display_pause(self):
        self.win.update_window(self.pause_elts["pause_text"],self.win.conf["center"][0] - len(self.pause_elts["pause_text"])//2,curses.LINES//3-1,curses.A_BOLD)
        self.win.update_window(self.pause_elts["pause_cmds"],self.win.conf["center"][0] - len(self.pause_elts["pause_cmds"])//2,curses.LINES//3)
        # Controls
        y=curses.LINES//4-4
        self.win.update_window(self.pause_elts["p1_cmds"][0],0,y,curses.A_BOLD)
        self.win.update_window(self.pause_elts["p2_cmds"][0],curses.COLS-1-len(self.pause_elts["p2_cmds"][0]),y,curses.A_BOLD)
        for i in range(1,len(self.pause_elts["p1_cmds"])):
            self.win.update_window(self.pause_elts["p1_cmds"][i],0,y+i)
            self.win.update_window(self.pause_elts["p2_cmds"][i],curses.COLS-1-len(self.pause_elts["p2_cmds"][i]),y+i)

    def _clear_pause(self):
        self.win.update_window(" " * len(self.pause_elts["pause_text"]),self.win.conf["center"][0] - len(self.pause_elts["pause_text"])//2,curses.LINES//3-1)
        self.win.update_window(" " * len(self.pause_elts["pause_cmds"]),self.win.conf["center"][0] - len(self.pause_elts["pause_cmds"])//2,curses.LINES//3)
        line_length = curses.COLS-1
        y = curses.LINES//4-4
        for i in range(len(self.pause_elts["p1_cmds"])):
            self.win.update_window(" " * line_length,0,y+i)

    def _display_player(self,player):
        base_y = curses.LINES-2
        self.win.update_window(player.body.foot.part,player.body.foot.pos[0],base_y-player.body.foot.pos[1])
        self.win.update_window(player.body.midlow.part,player.body.midlow.pos[0],base_y-player.body.midlow.pos[1])
        if player.player_type == "1":
            self.win.update_window(player.body.midtop.part[:-1],player.body.midtop.pos[0],base_y-player.body.midtop.pos[1])
            self.win.update_window(player.body.midtop.part[-1],player.body.midtop.pos[0] + player.body.midtop.length-1,base_y-player.body.midtop.pos[1],curses.color_pair(2))
        else:
            self.win.update_window(player.body.midtop.part[0],player.body.midtop.pos[0],base_y-player.body.midtop.pos[1],curses.color_pair(3))
            self.win.update_window(player.body.midtop.part[1:],player.body.midtop.pos[0]+1,base_y-player.body.midtop.pos[1])
        self.win.update_window(player.body.head.part,player.body.head.pos[0],base_y-player.body.head.pos[1])

    def _clear_player(self,player):
        base_y = curses.LINES-2
        self.win.update_window(" " * player.body.foot.length,player.body.foot.pos[0],y=base_y-player.body.foot.pos[1])
        self.win.update_window(" " * player.body.midlow.length,player.body.midlow.pos[0],y=base_y-player.body.midlow.pos[1])
        self.win.update_window(" " * player.body.midtop.length,player.body.midtop.pos[0],y=base_y-player.body.midtop.pos[1])
        self.win.update_window(" " * player.body.head.length,player.body.head.pos[0],y=base_y-player.body.head.pos[1])
    
    def _diplay_start(self,start_pos_scene):
        time.sleep(self.fps)
        # Scene
        self.win.update_window("=" * (self.scene.length),x=start_pos_scene,y=curses.LINES-1)

        time.sleep(self.fps)
        # Obstacles
        for i in self.obs:
            self.win.update_window("x",i,curses.LINES-2)
        
        # Player 1
        self.player1.pos = (start_pos_scene + self.scene.pos_p1,0)
        self._display_player(self.player1)

        # Player 2
        self.player2.pos = (start_pos_scene + self.scene.pos_p2,0)
        self._display_player(self.player2)

        # Score
        score_text = str(self.player1.score) + " | " + str(self.player2.score)
        self.win.update_window(score_text,curses.COLS//2 - len(score_text)//2,2*curses.LINES//3)
    
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
                self.actions.append((player,))
            elif chr(key) == 's':
                self._change_state(player,"blocking")
                self.actions.append((self.player1,time.time()))
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
                self.actions.append((player,))
            elif chr(key) == 'p':
                self._change_state(player,"blocking")
                self.actions.append((self.player2,time.time()))
            elif chr(key) == 'm':
                if not self._is_there_player(player,self.player2,1):
                    self._jump_right(player)
            elif chr(key) == 'l':
                if not self._is_there_player(player,self.player2,1):
                    self._jump_left(player)
    
    def _scored(self,text=""):
        # Score
        self.win.update_window(" " * (curses.COLS-1),0,2*curses.LINES//3)
        score_text = str(self.player1.score) + " | " + str(self.player2.score)
        self.win.update_window(score_text,curses.COLS//2 - len(score_text)//2,2*curses.LINES//3,curses.A_BOLD)

        self.actions = []

        self.win.update_window(text,self.win.conf["center"][0] - len(text)//2,curses.LINES//3)
        time.sleep(1)
        self._clear_player(self.player1)
        self.player1.pos = (self.scene_start + self.scene.pos_p1,0)
        self.player1.state = "rest"
        self._display_player(self.player1)

        self._clear_player(self.player2)
        self.player2.pos = (self.scene_start + self.scene.pos_p2,0)
        self.player2.state = "rest"
        self._display_player(self.player2)

        self.win.update_window(" " * (curses.COLS-1),0,curses.LINES//3)

    def _buffer_actions(self):
        current = time.time()
        if self.actions:
            for action in self.actions:
                player = action[0]
                if player.state == "blocking":
                    if current - action[1] >= player.blocking_time:
                        self._change_state(player,"rest")
                        self.actions.remove(action)
                elif player.state == "attacking":
                    if player.player_type == "1":
                        if self.player2.pos[0]-2 - self.player2.defending_range <= player.pos[0] + int(player.attacking_range) and self.player2.state != "blocking":
                            player.score += 1
                            self._scored("Player 1 scored!")
                    else:
                        if self.player1.pos[0]+2 + self.player1.defending_range >= player.pos[0] - int(player.attacking_range) and self.player1.state != "blocking":
                            player.score += 1
                            self._scored("Player 2 scored!")

                        
        
    def _is_there_obstacle(self,player,dir):
        if player.player_type == "1":
            if dir > 0:
                return (player.pos[0] + dir in self.obs) or (player.pos[0] + dir >= self.scene_end)
            return (player.body.foot.pos[0] + dir in self.obs) or (player.body.foot.pos[0] + dir <= self.scene_start)
        else:
            if dir > 0:
                return ((player.body.foot.pos[0] + player.body.foot.length) + dir in self.obs) or (player.body.foot.pos[0] + player.body.foot.length + dir) >= self.scene_end
            return (player.pos[0] + dir in self.obs) or (player.pos[0] + dir <= self.scene_start)

    def _is_there_player(self,player,target,dir):
        if dir > 0:
            return ((player.body.head.pos[0] + 1 + player.body.head.length) == target.body.head.pos[0])
        return (player.body.head.pos[0] - 1 == (target.body.head.pos[0] + target.body.head.length))
            
    def _move_right(self,player):
        time.sleep(self.fps*player.movement_speed)
        self._clear_player(player)
        player.pos = (player.pos[0]+1,player.pos[1])
        self._display_player(player)

    def _move_left(self,player):
        time.sleep(self.fps*player.movement_speed)
        self._clear_player(player)
        player.pos = (player.pos[0]-1,player.pos[1])
        self._display_player(player)
    
    def _jump_right(self,player):
        # Up
        time.sleep(self.fps*player.movement_speed)
        self._clear_player(player)
        player.pos = (player.pos[0],player.pos[1]+1)
        self._display_player(player)
        # Right 1
        time.sleep(self.fps*(player.movement_speed/2))
        self._clear_player(player)
        player.pos = (player.pos[0]+1,player.pos[1])
        self._display_player(player)
        # Right 2
        time.sleep(self.fps*(player.movement_speed/2))
        self._clear_player(player)
        player.pos = (player.pos[0]+1,player.pos[1])
        self._display_player(player)
        # Right 3
        # time.sleep(self.fps*(player.movement_speed/3))
        # self._clear_player(player)
        # player.pos = (player.pos[0]+1,player.pos[1])
        # self._display_player(player)
        # Down
        time.sleep(self.fps*player.movement_speed)
        self._clear_player(player)
        player.pos = (player.pos[0],player.pos[1]-1)
        self._display_player(player)

    def _jump_left(self,player):
        # Up
        time.sleep(self.fps*player.movement_speed)
        self._clear_player(player)
        player.pos = (player.pos[0],player.pos[1]+1)
        self._display_player(player)
        # Left 1
        time.sleep(self.fps*(player.movement_speed/2))
        self._clear_player(player)
        player.pos = (player.pos[0]-1,player.pos[1])
        self._display_player(player)
        # Left 2
        time.sleep(self.fps*(player.movement_speed/2))
        self._clear_player(player)
        player.pos = (player.pos[0]-1,player.pos[1])
        self._display_player(player)
        # Left 3
        # time.sleep(self.fps*(player.movement_speed/3))
        # self._clear_player(player)
        # player.pos = (player.pos[0]-1,player.pos[1])
        # self._display_player(player)
        # Down
        time.sleep(self.fps*player.movement_speed)
        self._clear_player(player)
        player.pos = (player.pos[0],player.pos[1]-1)
        self._display_player(player)

    def _save(self):
        conf  = {
            "scene": {"length": self.scene.length, "obs": self.scene.pos_obs},
            "player1": {""}
        }
        pass

    def _change_state(self, player,state):
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
    @property
    def paused(self):
        return self.__paused
    @paused.setter
    def paused(self,paused):
        self.__paused = paused
    @property
    def loaded_from_save(self):
        return self.__loaded_from_save
    @loaded_from_save.setter
    def loaded_from_save(self,loaded_from_save):
        self.__loaded_from_save = loaded_from_save
    @property
    def pause_elts(self):
        return self.__pause_elts
    @pause_elts.setter
    def pause_elts(self,pause_elts):
        self.__pause_elts = pause_elts
    @property
    def actions(self):
        return self.__actions
    @actions.setter
    def actions(self,actions):
        self.__actions = actions