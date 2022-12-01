import copy
class Scene:
    def __init__(self,pattern):
        self.__len = len(pattern)
        self.__p1 = pattern.index('1')
        self.__p2 = pattern.index('2')
        self.__obs = tuple([i for i,char in enumerate(pattern) if char == 'x'])
        self.__pattern = pattern
    
    @property
    def length(self):
        return copy.copy(self.__len)
    @property
    def pos_p1(self):
        return copy.copy(self.__p1)
    @property
    def pos_p2(self):
        return copy.copy(self.__p2)
    @property
    def pos_obs(self):
        return copy.deepcopy(self.__obs)
    @property
    def pattern(self):
        return copy.copy(self.__pattern)