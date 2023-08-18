from unittest import TestCase
from levelup.map import GameMap


class TestGetPosition(TestCase):
    def test_calculatePosition_forward(self):
        initalPosition = [3, "f"]
        moveDirection = "F"
        testObj = GameMap.calculatePosition(initalPosition, moveDirection)
        self.assertEqual(testObj, [1, "e"])

    def test_calculatePosition_back(self):
        initalPosition = [3, "f"]
        moveDirection = "B"
        testObj = GameMap.calculatePosition(initalPosition, moveDirection)
        self.assertEqual(testObj, [1, "g"])

    def test_calculatePosition_left(self):
        initalPosition = [3, "f"]
        moveDirection = "L"
        testObj = GameMap.calculatePosition(initalPosition, moveDirection)
        self.assertEqual(testObj, [2, "f"])

    def test_calculatePosition_right(self):
        initalPosition = [3, "f"]
        moveDirection = "R"
        testObj = GameMap.calculatePosition(initalPosition, moveDirection)
        self.assertEqual(testObj, [4, "f"])

    def test_isPositionValid(self):
        pass