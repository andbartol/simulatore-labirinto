import unittest
import robot
import mappa

class TestRobot(unittest.TestCase):
    def test_robot_creation(self):
        m = mappa.Mappa()
        r = robot.Robot(m, (15,15))

    def test_sensor_forward(self):
        m = mappa.Mappa()
        m.load("maps/mappaSensori.map")
        r = robot.Robot(m, (15,15))
        self.assertAlmostEqual(r.sense(robot.Sensor.FORWARD), 15.0, 0.1)

if __name__ == '__main__':
    unittest.main()
