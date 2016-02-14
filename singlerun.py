import math
import pygame
import mappa
import robot
import math

class SingleRun():
    def __init__(self, robot, scale=1):
        self.robot = robot
        self.scale = scale

    def set_scale(self, scale):
        self.scale = scale

    def play(self):

        self.screen = pygame.display.set_mode((1024,768))
        pygame.display.set_caption("ROBITIS")
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 30)

        while True:
            self.update()
            self.draw()

            try:
                pygame.display.flip()
            except Exception:
                pygame.display.quit()
                break

    def update(self):
        self.robot.run()

    def draw(self):
        self.screen.fill((0,0,0))
        self.drawMappa()
        self.drawRobot()
        self.drawSensors()

    def drawMappa(self):
        for linea in self.robot.mappa.linee:
            l0 = []
            l0.append(linea[0][0] * self.scale)
            l0.append(linea[0][1] * self.scale)
            l1 = []
            l1.append(linea[1][0] * self.scale)
            l1.append(linea[1][1] * self.scale)

            pygame.draw.line(self.screen, (255,255,255), l0, l1)

    def drawSensors(self):
        for sensor in robot.Sensor:
            sur = self.renderSensor(sensor)
            self.screen.blit(sur, (500, sensor.value*30))

    def renderSensor(self, sensor):
        testo = sensor.__str__() + ": "
        testo += str(self.robot.sense(sensor))
        return self.font.render(testo, False, (255,255,255))

    def drawRobot(self):
        radius = 10
        pos_adj = (self.robot.position[0]*self.scale, self.robot.position[1]*self.scale)
        pygame.draw.circle(self.screen, (0,255,0), pos_adj, radius, 1)
        angle = self.robot.angle
        end = (radius*math.cos(angle)+pos_adj[0], radius*math.sin(angle)+pos_adj[1])
        pygame.draw.line(self.screen, (255,0,0), pos_adj, end)

def test():
    m = mappa.Mappa()
    m.load("maps/mappaSensori.map")

    r = robot.Robot(m, (15,15))
    r.turn(math.pi)

    run = SingleRun(r, scale=10)
    run.play()

if __name__ == '__main__':
    test()
