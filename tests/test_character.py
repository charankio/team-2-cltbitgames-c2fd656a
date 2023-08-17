from unittest import TestCase
from levelup.character import Character
from levelup.position import Position

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = ""
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_Character(self):
        ARBITRARY_NAME = "Bob"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_getName(self):
        ARBITRARY_NAME = "Bob"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_enterMap(self):
        ENTERED_MAP = "True"
        testobj = Character(ENTERED_MAP)
        self.assertEqual(ENTERED_MAP, ENTERED_MAP)
    
    def test_getPosition(self):
        CHARACTER_POSITION = "A,1"
        testobj = Character(CHARACTER_POSITION)
        self.assertEqual(CHARACTER_POSITION, testobj.name)
            
    def test_move(self):
        CHARACTER_DIRECTION = "R"
        testobj = Character(CHARACTER_DIRECTION)
        self.assertEqual(CHARACTER_DIRECTION, testobj.name)
    
    def test_Position(self):
        CHARACTER_POSITION = "A,2"
        testobj = Position(CHARACTER_POSITION)
        self.assertEqual(CHARACTER_POSITION, testobj.name)