from unittest import TestCase
from levelup.character import Character

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = ""
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_string(self):
        ARBITRARY_NAME = "Bob"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_getName(self):
        ARBITRARY_NAME = "Uncle"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_enterMap(self):
        ENTERED_MAP = True
        testobj = Character(ENTERED_MAP)
        self.assertEqual(ENTERED_MAP, testobj.name)
    


    