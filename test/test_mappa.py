import unittest
import mappa

class TestMappa(unittest.TestCase):
    def test_load(self):
        m = mappa.Mappa((500,500))
        m.load("maps/mappaDef.map")
        with self.assertRaises(OSError):
            m.load("maps/mappanonesistente.map")

    def test_loaded_map_line(self):
        m = mappa.Mappa((400,400))
        m.load("maps/mappaTestLine.map")
        for x in range(10):
            self.assertTrue(m.get((x, 0)))
        self.assertFalse(m.get((10,0)))


if __name__ == '__main__':
    unittest.main()
