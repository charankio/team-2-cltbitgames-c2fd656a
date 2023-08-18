import logging

class GameMap:
    
    def __init__(self):
        numPositions = 100

    def getPositions(self):
        return [1, "a"]

    def calculatePosition(startingPosition: dict, moveDirection: str):
        moveDirection = moveDirection.lower()
        newPosition = []
    
        if moveDirection == "f":
            startingPosition[1] 
        elif moveDirection == "b":
            pass
        elif moveDirection == "l":
            pass
        elif moveDirection == "r":
            pass

        return [1, "b"]

    @staticmethod
    def isPositionValid(newPosition: dict):
        return False