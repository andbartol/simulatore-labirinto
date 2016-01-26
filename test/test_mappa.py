import unittest
import mappa

class TestMappa(unittest.TestCase):
    def test_load(self):
        m = mappa.Mappa()
        m.load("maps/mappaDef.map")
        with self.assertRaises(OSError):
            m.load("maps/mappanonesistente.map")

    def test_loaded_map_line(self):
        m = mappa.Mappa()
        m.load("maps/mappaTestLine.map")
        self.assertTrue(((0.0,0.0),(9.0,0.0)) in m.linee, "Errore assert: " + str(m.linee))

if __name__ == '__main__':
    unittest.main()
