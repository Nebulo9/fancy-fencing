from copy import copy
class Player:
    def __init__(self,type,movement_speed,attacking_range,defending_range,blocking_time):
        self.__type = type
        self.__ms = movement_speed
        self.__ar = attacking_range
        self.__dr = defending_range
        self.__bt = blocking_time
        self.__pos = -1

    @property
    def type(self):
        return copy(self.__type)
    @property
    def movement_speed(self):
        return copy(self.__ms)
    @property
    def attacking_range(self):
        return copy(self.__ar)
    @property
    def defending_range(self):
        return copy(self.__dr)
    @property
    def blocking_time(self):
        return copy(self.__bt)
    @property
    def pos(self):
        return copy(self.__pos)
    @pos.setter
    def pos(self, pos):
        self.__pos = pos
