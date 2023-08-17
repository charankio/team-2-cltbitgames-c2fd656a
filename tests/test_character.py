from unittest import TestCase
from levelup.character import Character

class FakeGameMap():

    xCoordinate = "x"
    yCoordiante = "y"

    def calculatePosition():
        

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = ""
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)
    
    def test_enterMap(self):
        testObj = Character.enterMap()
        self.assertFalse(testObj)
    
    def test_move(self):
        charPOS = Character.cpos = [1, 5]
        moveDirection = "L"
        testObj = charPOS.move(moveDirection)
        self.assertEqual([1, 4], testObj)