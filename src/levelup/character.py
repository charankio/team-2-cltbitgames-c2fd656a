from levelup.map import GameMap

class Character:

    def __init__(self, character_name):
        self.name = character_name
        self.cpos = []
        self.map = GameMap()


    @staticmethod
    def enterMap():
        pass
    
    #@staticmethod
    def move(self, moveDirction):
        ##pass
        self.cpos = self.map.calculatePosition(self.cpos, moveDirction)

  