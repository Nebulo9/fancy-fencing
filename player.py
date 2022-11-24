from copy import copy
class Player:
    def __init__(self,_type: str,movement_speed: float,attacking_range: float,defending_range: float,blocking_time: float):
        self.__type = _type
        self.__ms = movement_speed
        self.__ar = attacking_range
        self.__dr = defending_range
        self.__bt = blocking_time
        self.__state = "rest"
        self.__pos = -1
        self.__body = Body(self.player_type,self.pos)

    @property
    def player_type(self):
        return self.__type
    @property
    def movement_speed(self):
        return self.__ms
    @property
    def attacking_range(self):
        return self.__ar
    @property
    def defending_range(self):
        return self.__dr
    @property
    def blocking_time(self):
        return self.__bt
    @property
    def body(self):
        return self.__body
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self,state):
        self.__state = state
        self.body.change(self.state)
    @property
    def pos(self):
        return self.__pos
    @pos.setter
    def pos(self, pos):
        self.__pos = pos

class Body:
    def __init__(self,_type: str,pos: int):
        self.__type = _type
        head_part = "<O O>"
        self.__head = BodyPart(pos-len(head_part)//2,head_part)
        self.__midlow = BodyPart(pos,"|")
        if(self.player_type == "1"):
            self.__foot = BodyPart(pos-1,"/|")
            self.__midtop = BodyPart(pos-2,"|_/")
        else:
            self.__foot = BodyPart(pos-1,"|\\")
            self.__midtop = BodyPart(pos-2,"\\_|")
    @property
    def player_type(self):
        return self.__type
    @property
    def head(self):
        return self.__head
    @property
    def midlow(self):
        return self.__midlow
    @property
    def foot(self):
        return self.__foot
    @property
    def midtop(self):
        return self.__midtop
    @midtop.setter
    def midtop(self,midtop):
        self.__midtop = midtop
    
    def change(self,state):
        if state == "rest":
            self.midtop.part = "|_/"
        elif state == "attacking":
            self.midtop.part = "|__"
        elif state == "blocking":
            self.midtop.part = "|_|"

class BodyPart:
    def __init__(self,pos: int,part: str):
        self.__pos = pos
        self.__part = part
    @property
    def pos(self):
        return self.__pos
    @pos.setter
    def pos(self,pos):
        self.__pos = pos
    @property
    def part(self):
        return self.__part
    @part.setter
    def part(self,part):
        self.__part = part