import unittest
import math
import pickle
import squarerobot

class TestRobot(unittest.TestCase):
    def setUp(self):
        with open("prova.map", "rb") as f:
            map = pickle.load(f)
        self.robot = squarerobot.SquareRobot(map, [0,0])

    def test_turn(self):
        self.robot.turn(squarerobot.Direction.BACK)
        self.assertEqual(self.robot.direction, squarerobot.Direction.BACK)

    def test_move_no_walls(self):
        self.robot.move()
        self.assertEqual(self.robot.position, [0,1])

    def test_sensor_back(self):
        dist = self.robot.sense(squarerobot.Direction.BACK)
        self.assertEqual(dist, 0, self.robot.mappa)

    def test_sensor_forward(self):
        dist = self.robot.sense(squarerobot.Direction.FORWARD)
        self.assertEqual(dist, 5, self.robot.mappa)

    def test_sensor_left(self):
        dist = self.robot.sense(squarerobot.Direction.LEFT)
        self.assertEqual(dist, 0, self.robot.mappa)

    def test_sensor_right(self):
        dist = self.robot.sense(squarerobot.Direction.RIGHT)
        self.assertEqual(dist, 1, self.robot.mappa)

    def test_sensor_back_movement(self):
        self.robot.move()
        dist = self.robot.sense(squarerobot.Direction.BACK)
        self.assertEqual(dist, 1, self.robot.mappa)

    def test_move_walls(self):
        self.robot.move()
        self.robot.turn(squarerobot.Direction.BACK)
        self.robot.move()
        self.robot.move()
        self.assertEqual(self.robot.position, [0,0])

    def test_move_walls_forward(self):
        for i in range(10):
            self.robot.move()
        self.assertEqual(self.robot.position, [0,5])

    def test_move_walls_right(self):
        self.robot.turn(squarerobot.Direction.RIGHT)
        for i in range(10):
            self.robot.move()
        self.assertEqual(self.robot.position, [1,0])

    def test_move_walls_left(self):
        self.robot.turn(squarerobot.Direction.LEFT)
        for i in range(10):
            self.robot.move()
        self.assertEqual(self.robot.position, [0,0])

    def test_move_path(self):
        for i in range(3):
            self.robot.move()
        self.robot.turn(squarerobot.Direction.RIGHT)
        for i in range(10):
            self.robot.move()
        self.assertEqual(self.robot.position, [5,3])

if __name__ == '__main__':
    unittest.main()
