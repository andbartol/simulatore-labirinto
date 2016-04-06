import unittest
import robot2
import maputilities
import pickle

class TestRobot2(unittest.TestCase):

    def setUp(self):
        with open("prova.map", "rb") as f:
            self.map = pickle.load(f)
        self.robot = robot2.Robot2(self.map)

    def test_sensors(self):
        self.robot.position = [0,0]
        self.assertEqual(self.robot.sense(), [True,True,False,True])

    def test_sensors_2(self):
        self.robot.position = [1,0]
        self.assertEqual(self.robot.sense(), [True,False,False,True])

    def test_free_movement(self):
        self.robot.position = [0,0]
        self.robot.move(2)
        self.assertEqual(self.robot.position, [0,1])

    def test_wall_movement(self):
        self.robot.position = [0,0]
        self.robot.move(0)
        self.assertEqual(self.robot.position, [0, 0])
        self.robot.move(1)
        self.assertEqual(self.robot.position, [0, 0])
        self.robot.move(3)
        self.assertEqual(self.robot.position, [0, 0])

    def test_block_outer(self):
        self.assertTrue(maputilities.is_outer_block([0,0], self.map, [15,15]))
        self.assertFalse(maputilities.is_outer_block([1,5], self.map, [15,15]))
        self.assertTrue(maputilities.is_outer_block([2,5], self.map, [15,15]))
        self.assertFalse(maputilities.is_outer_block([5,7], self.map, [15,15]))


if __name__ == '__main__':
    unittest.main()
