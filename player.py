from copy import copy
class Player:
    def __init__(self,_type: str,movement_speed: float,attacking_range: float,defending_range: float,blocking_time: float):
        self.__type = _type
        self.__ms = movement_speed
        self.__ar = attacking_range
        self.__dr = defending_range
        self.__bt = blocking_time
        self.__pos = -1

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
    def pos(self):
        return self.__pos
    @pos.setter
    def pos(self, pos):
        self.__pos = pos
