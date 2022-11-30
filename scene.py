class Scene:
    def __init__(self,pattern):
        self.__len = len(pattern)
        self.__p1 = pattern.index('1')
        self.__p2 = pattern.index('2')
        self.__obs = tuple([i for i,char in enumerate(pattern) if char == 'x'])
    
    @property
    def length(self):
        return self.__len
    @property
    def pos_p1(self):
        return self.__p1
    @property
    def pos_p2(self):
        return self.__p2
    @property
    def pos_obs(self):
        return self.__obs