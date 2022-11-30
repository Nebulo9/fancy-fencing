import copy
class Player:
    def __init__(self,_type,movement_speed,attacking_range,defending_range,blocking_time):
        self.__type = _type
        self.__ms = movement_speed
        self.__ar = attacking_range
        self.__dr = defending_range
        self.__bt = blocking_time
        self.__state = "rest"
        self.__pos = (0,0)
        self.__body = Body(self.player_type,self.pos)
        self.__score = 0

    @property
    def player_type(self):
        return copy.copy(self.__type)
    @property
    def movement_speed(self):
        return copy.copy(self.__ms)
    @property
    def attacking_range(self):
        return copy.copy(self.__ar)
    @property
    def defending_range(self):
        return copy.copy(self.__dr)
    @property
    def blocking_time(self):
        return copy.copy(self.__bt)
    @property
    def body(self):
        return self.__body
    @property
    def score(self):
        return copy.copy(self.__score)
    @score.setter
    def score(self,score):
        self.__score = score
    @property
    def state(self):
        return copy.copy(self.__state)
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
        self.body.head.pos = (self.pos[0] - self.body.head.length//2,self.pos[1] + 3)
        if self.player_type == "1":
            self.body.midtop.pos = (self.pos[0],self.pos[1]+2)
            self.body.midlow.pos = (self.pos[0],self.pos[1]+1)
            self.body.foot.pos = (self.pos[0] - 1,self.pos[1])
        else:
            self.body.midtop.pos = (self.pos[0] - 2,self.pos[1]+2)
            self.body.midlow.pos = (self.pos[0],self.pos[1]+1)
            self.body.foot.pos = (self.pos[0],self.pos[1])

class Body:
    def __init__(self,_type,pos):
        self.__type = _type
        head_part = "<o>"
        self.__head = BodyPart((pos[0]-len(head_part)//2,pos[1]+3),head_part)
        self.__midlow = BodyPart((pos[0],pos[1]+1),"|")
        if(self.player_type == "1"):
            self.__foot = BodyPart((pos[0]-1,pos[1]),"/|")
            self.__midtop = BodyPart((pos[0],pos[1]+2),"|_/")
        else:
            self.__foot = BodyPart((pos[0],pos[1]),"|\\")
            self.__midtop = BodyPart((pos[0]-2,pos[1]+2),"\\_|")
    @property
    def player_type(self):
        return copy.copy(self.__type)
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
        """Changes the value of the midtop part string depending on the state"""
        if state == "rest":
            if self.player_type == "1":
                self.midtop.part = "|_/"
            else:
                self.midtop.part = "\\_|"
        elif state == "attacking":
            if self.player_type == "1":
                self.midtop.part = "|__"
            else:
                self.midtop.part = "__|"
        elif state == "blocking":
            self.midtop.part = "|_|"

class BodyPart:
    def __init__(self,pos,part):
        self.__pos = pos
        self.__part = part
        self.__length = len(self.part)
    @property
    def length(self):
        return copy.copy(self.__length)
    @property
    def pos(self):
        return copy.copy(self.__pos)
    @pos.setter
    def pos(self,pos):
        self.__pos = pos
    @property
    def part(self):
        return copy.copy(self.__part)
    @part.setter
    def part(self,part):
        self.__part = part