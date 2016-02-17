from enum import Enum
import math
import line

class Sensor(Enum):
    FORWARD = 1
    LEFT = 2
    RIGHT = 3
    BACK = 4
    def offset_angle(self):
        if self.name == "FORWARD":
            return 0
        if self.name == "LEFT":
            return math.pi/2
        if self.name == "RIGHT":
            return -math.pi/2
        if self.name == "BACK":
            return math.pi

class Robot():
    """
    Classe standard del Robot da ereditare, per usarlo bisogna fare
    l'override del metodo run
    """
    def __init__(self, mappa, position):
        self.mappa = mappa
        self.position = position
        self.angle = math.pi/2
        self.velocity = 1

    def run(self):
        '''
        OVERRIDE ME
        '''
        pass

    def move(self):
        dist = self.sense(Sensor.FORWARD)
        if dist <= self.velocity or dist <= 0.1:
            velocity = dist-0.1
        else:
            velocity = self.velocity
        dx = velocity*math.cos(self.angle)
        dy = velocity*math.sin(self.angle)
        self.position[0] += dx
        self.position[1] += dy

    def sense(self, sensor):
        #https://web.archive.org/web/20120612145751/http://local.wasp.uwa.edu.au/~pbourke/geometry/lineline2d/
        #Crea un sensore che parte dal robot e punta all'angolo self.angle
        v_sensor = [self.position[0]+math.cos(self.angle+sensor.offset_angle()), self.position[1]+math.sin(self.angle+sensor.offset_angle())]
        distances = []
        for linea in self.mappa.linee:
            # Controlla la distanza tra la linea e a linea della mappa
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
                #Calcolo della distanza
                x = self.position[0]+ua*(v_sensor[0]-self.position[0])
                y = self.position[1]+ua*(v_sensor[1]-self.position[1])
                dx = x - self.position[0]
                dy = y - self.position[1]
                dist_squared =  dx**2 + dy**2
                distances.append(dist_squared)
        try:
            return math.sqrt(min(distances))
        except ValueError as e:
            return 9999

    def turn(self, angle):
        self.angle += angle
