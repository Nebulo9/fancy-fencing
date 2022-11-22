from copy import copy,deepcopy
class Scene:
    def __init__(self,pattern: str):
        self.__len = len(pattern)
        self.__p1 = pattern.index('1')
        self.__p2 = pattern.index('2')
        self.__obs = [i for i,char in enumerate(pattern) if char == 'x']
    
    @property
    def length(self):
        return copy(self.__len)
    @property
    def pos_p1(self):
        return copy(self.__p1)
    @property
    def pos_p2(self):
        return copy(self.__p2)
    @property
    def pos_obs(self):
        return deepcopy(self.__obs)