import unittest
import robot
import mappa
import math

class TestRobot(unittest.TestCase):
    def test_robot_creation(self):
        m = mappa.Mappa()
        r = robot.Robot(m, (15,15))

    def test_sensor_forward(self):
        m = mappa.Mappa()
        m.load("maps/mappaSensori.map")
        r = robot.Robot(m, (15,15))
        dist_r = r.sense(robot.Sensor.FORWARD)
        self.assertAlmostEqual(dist_r, 15, delta=0.1)

    def test_turn_sensor(self):
        m = mappa.Mappa()
        m.load("maps/mappaSensori.map")
        r = robot.Robot(m, (15,15))
        r.turn(-(45/180)*math.pi)
        dist_r = r.sense(robot.Sensor.FORWARD)
        self.assertAlmostEqual(dist_r, 15.55, delta=0.1)

    def test_sensor_left(self):
        m = mappa.Mappa()
        m.load("maps/mappaSensori.map")
        r = robot.Robot(m, (15,15))
        dist_r = r.sense(robot.Sensor.LEFT)
        self.assertAlmostEqual(dist_r, 13.0, delta=0.1)

    def test_sensor_right(self):
        m = mappa.Mappa()
        m.load("maps/mappaSensori.map")
        r = robot.Robot(m, (15,15))
        dist_r = r.sense(robot.Sensor.RIGHT)
        self.assertAlmostEqual(dist_r, 11.0, delta=0.1)

    def test_sensor_back(self):
        m = mappa.Mappa()
        m.load("maps/mappaSensori.map")
        r = robot.Robot(m, (15,15))
        dist_r = r.sense(robot.Sensor.BACK)
        self.assertAlmostEqual(dist_r, 12.0, delta=0.1)

if __name__ == '__main__':
    unittest.main()
