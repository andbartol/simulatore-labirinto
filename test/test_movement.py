import unittest
import mappa
import robot
import math

class TestMovement(unittest.TestCase):
    def setUp(self):
        self.m = mappa.Mappa()
        self.m.load("maps/mappaSensori.map")
        self.r = robot.Robot(self.m,[15,15])

    def test_movement(self):
        self.r.velocity = 0.1
        self.r.move()
        self.assertAlmostEqual(self.r.position[0], 15.0)
        self.assertAlmostEqual(self.r.position[1], 15.1)
        self.r.velocity = 0.2
        self.r.move()
        self.assertAlmostEqual(self.r.position[0], 15.0)
        self.assertAlmostEqual(self.r.position[1], 15.3)

    def test_movement_turn(self):
        self.r.velocity = 0.1
        self.r.turn(math.pi/2)
        self.r.move()
        dist = self.r.sense(robot.Sensor.FORWARD)
        self.assertAlmostEqual(dist, 12.9)

    def test_movement_wall(self):
        self.r.velocity = 1
        for i in range(17):
            self.r.move()
        self.assertAlmostEqual(self.r.position[0], 15)
        self.assertAlmostEqual(self.r.position[1], 29.9)

    def test_movement_wall_slow(self):
        self.r.velocity = 0.05
        for i in range(311):
            self.r.move()
        self.assertAlmostEqual(self.r.position[0], 15)
        self.assertAlmostEqual(self.r.position[1], 29.9)

    def test_movement_wall_fast(self):
        self.r.velocity = 1000
        for i in range(311):
            self.r.move()
        self.assertAlmostEqual(self.r.position[0], 15)
        self.assertAlmostEqual(self.r.position[1], 29.9)

if __name__ == '__main__':
    unittest.main()
