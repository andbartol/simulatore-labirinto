from enum import Enum
import math
import line

class Sensor(Enum):
    FORWARD = 1

class Robot():
    def __init__(self, mappa, position):
        self.mappa = mappa
        self.position = position

    def sense(self, sensor):
        #https://web.archive.org/web/20120612145751/http://local.wasp.uwa.edu.au/~pbourke/geometry/lineline2d/
        v_sensor = [self.position[0], self.position[1]+40]
        distances = []
        for linea in self.mappa.linee:
            denominatore = (linea[1][1]-linea[0][1])*(v_sensor[0]-self.position[0])-(linea[1][0]-linea[0][0])*(v_sensor[1]-self.position[1])
            numa = (linea[1][0]-linea[0][0])*(self.position[1]-linea[0][1])-(linea[1][1]-linea[0][1])*(self.position[0]-linea[0][0])
            numb = (v_sensor[0]-self.position[0])*(self.position[1]-linea[0][1])-(v_sensor[1]-self.position[1])*(self.position[0]-linea[0][0])
            try:
                ua = numa/denominatore
                ub = numb/denominatore
            except ZeroDivisionError:
                #Le linee sono parallele, passiamo alla prossima
                continue
            if ua > 0 and 0 <= ub <= 1:
                x = self.position[0]+ua*(v_sensor[0]-self.position[0])
                y = self.position[1]+ua*(v_sensor[1]-self.position[1])
                dx = x - self.position[0]
                dy = y - self.position[1]
                dist_squared =  dx**2 + dy**2
                distances.append(dist_squared)
        return math.sqrt(min(distances))
