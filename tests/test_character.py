from unittest import TestCase
from levelup.character import Character

class FakeGameMap():

    xCoordinate = "x"
    yCoordiante = "y"

    def calculatePosition(self, arg1, arg2):
        return [1, 4]
        

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = ""
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)
    
    def test_enterMap(self):
        testObj = Character.enterMap()
        self.assertFalse(testObj)
    
    def test_move(self):
        ARBITRARY_NAME = ""
        char = Character(ARBITRARY_NAME)
        char.cpos = [1, 5]
        char.map = FakeGameMap()

        moveDirection = "L"
        testObj = char.move(moveDirection)
        testObj = char.cpos
        self.assertEqual([1, 4], testObj)