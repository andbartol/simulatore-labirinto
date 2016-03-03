from enum import Enum
import math
import line

class Direction(Enum):
    FORWARD = 1
    LEFT = 2
    RIGHT = 3
    BACK = 4

class SquareRobot():
    """
    Classe standard del Robot da ereditare, per usarlo bisogna fare
    l'override del metodo run
    """
    def __init__(self, mappa, position):
        self.mappa = mappa
        self.position = position
        self.direction = Direction.FORWARD
        self.velocity = 1

    def run(self):
        '''
        OVERRIDE ME
        '''
        pass

    def move(self):
        dist = self.sense(self.direction)
        if self.direction == Direction.FORWARD:
            self._move_vertical_walls(dist, self.velocity)
        elif self.direction == Direction.BACK:
            self._move_vertical_walls(dist, -self.velocity)
        elif self.direction == Direction.RIGHT:
            self._move_horizontal_walls(dist, self.velocity)
        elif self.direction == Direction.LEFT:
            self._move_horizontal_walls(dist, -self.velocity)

    def _move_horizontal(self, velocity):
        self.position = [self.position[0]+velocity, self.position[1]]

    def _move_horizontal_walls(self, dist, velocity):
        if dist >= abs(velocity):
            self._move_horizontal(velocity)
        else:
            self._move_horizontal(dist)

    def _move_vertical(self, velocity):
        self.position = [self.position[0], self.position[1]+velocity]

    def _move_vertical_walls(self, dist, velocity):
        if dist >= abs(velocity):
            self._move_vertical(velocity)
        else:
            self._move_vertical(dist)

    def sense(self, sensor):
        if sensor == Direction.FORWARD or sensor == Direction.BACK:
            return self._sense_vertical(sensor)
        if sensor == Direction.LEFT or sensor == Direction.RIGHT:
            return self._sense_horizontal(sensor)

    def _sense_horizontal(self, sensor):
        x  = self.position[0]
        y0 = self.position[1]
        y1 = self.position[1]+1
        if sensor == Direction.RIGHT:
            x += 1
        for i in range(999):
            if [[x,y0],[x,y1]] in self.mappa or [[x,y1],[x,y0]] in self.mappa:
                return i
            if sensor == Direction.RIGHT:
                x += 1
            if sensor == Direction.LEFT:
                x -= 1

    def _sense_vertical(self, sensor):
        x0 = self.position[0]
        x1 = self.position[0]+1
        y  = self.position[1]
        if sensor == Direction.FORWARD:
            y += 1
        for i in range(999):
            if [[x0,y],[x1,y]] in self.mappa or [[x1,y], [x0,y]] in self.mappa:
                return i
            if sensor == Direction.FORWARD:
                y += 1
            if sensor == Direction.BACK:
                y -= 1

    def turn(self, direction):
        self.direction = direction
