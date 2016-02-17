import math
import pygame
import mappa
import robot
import math
import sys

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
        clock = pygame.time.Clock()

        while True:
            clock.tick(30)
            self.update()
            self.draw()

            pygame.display.flip()

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
        radius = 20
        pos_adj = (int(self.robot.position[0]*self.scale), int(self.robot.position[1]*self.scale))
        pygame.draw.circle(self.screen, (0,255,0), pos_adj, radius, 1)
        angle = self.robot.angle
        end = (int(radius*math.cos(angle)+pos_adj[0]), int(radius*math.sin(angle)+pos_adj[1]))
        pygame.draw.line(self.screen, (255,0,0), pos_adj, end)


def test():
    m = mappa.Mappa()
    m.load("maps/mappaDef.map")

    r = robot.Robot(m, [15,15])
    r.velocity = 4
    r.turn(3/16*(math.pi))
    robot.Robot.run = lambda a: keyboardMove(a)

    run = SingleRun(r, scale=1)
    run.play()


def keyboardMove(robot):
    if keyboardMove.turning_right:
        robot.turn(0.1)
    if keyboardMove.turning_left:
        robot.turn(-0.1)
    if keyboardMove.moving:
        robot.move()
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        if event.key == pygame.K_ESCAPE:
            pygame.display.quit()
            sys.exit(0)
        if event.key == pygame.K_UP:
            keyboardMove.moving = (event.type == pygame.KEYDOWN)
        if event.key == pygame.K_LEFT:
            keyboardMove.turning_left = (event.type == pygame.KEYDOWN)
        if event.key == pygame.K_RIGHT:
            keyboardMove.turning_right = (event.type == pygame.KEYDOWN)

keyboardMove.turning_right = False
keyboardMove.turning_left = False
keyboardMove.moving = False

if __name__ == '__main__':
    test()
