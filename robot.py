from enum import Enum
import line

class Sensor(Enum):
    FORWARD = 1

class Robot():
    def __init__(self, mappa, position):
        self.mappa = mappa
        self.position = position

    def sense(self, sensor):
        line_points = line.gen_line(self.position, (self.position[0], self.mappa.dimensione[1]))
        for index, point in enumerate(line_points):
            if self.mappa.get(point) == True:
                return index
        return 1000.0
