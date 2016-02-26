import math
import pygame
import mappa
import robot
import math
import sys
import pickle
import argparse

class MapCreator(object):
    def __init__(self, size=(30,30), output="a.map", input="a.map", tile_size=40):
        self.output = output
        self.size = size
        self.tile_size = tile_size
        self.horizontal = True
        self.pointer = [(0,0),(0,1)]
        if input != None:
            with open(input, "rb") as f:
                self.map = pickle.load(f)
        else:
            self.map = []

    def run(self):
        self.init_screen()
        self.init_font()
        clock = pygame.time.Clock()

        self.exit = False
        while not self.exit:
            clock.tick(120)
            self.update()
            self.draw()
            pygame.display.flip()
            self.manage_inputs()

        with open(self.output, "wb") as f:
            pickle.dump(self.map, f)

    def init_screen(self):
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption("ROBITIS MAP CREATOR")

    def init_font(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 30)

    def update(self):
        pass

    def manage_inputs(self):
        for event in pygame.event.get():
            if hasattr(event, 'key'):
                self.manage_keyboard(event)
            if hasattr(event, 'buttons'):
                self.manage_mouse(event)

    def manage_mouse(self, event):
        self.updatePointer(event)
        sel = [[y/self.tile_size for y in x] for x in self.pointer]
        if event.buttons[0] == 1:
            self.map.append(sel)
        elif event.buttons[2] == 1:
            try:
                self.map.remove(sel)
            except ValueError:
                pass

    def updatePointer(self, event):
        x = event.pos[0]/self.tile_size
        y = event.pos[1]/self.tile_size
        if self.horizontal:
            y = round(y)*self.tile_size
            start_x = math.floor(x)*self.tile_size
            end_x = math.ceil(x)*self.tile_size
            self.pointer = [(start_x, y), (end_x, y)]
        else:
            x = round(x)*self.tile_size
            start_y = math.floor(y)*self.tile_size
            end_y = math.ceil(y)*self.tile_size
            self.pointer = [(x, start_y), (x, end_y)]


    def manage_keyboard(self, event):
        if event.key == pygame.K_ESCAPE:
            pygame.display.quit()
            self.exit = True
        if event.key == pygame.K_SPACE and event.type == pygame.KEYDOWN:
            self.horizontal = not(self.horizontal)

    def draw(self):
        self.screen.fill((0,0,0))
        pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(0,0,self.size[0]*self.tile_size, self.size[1]*self.tile_size))
        self.draw_walls()
        self.draw_pointer()

    def draw_pointer(self):
        pygame.draw.line(self.screen, (255,0,218), self.pointer[0], self.pointer[1])

    def draw_walls(self):
        for wall in self.map:
            self.draw_wall(wall)

    def draw_wall(self, wall):
        start = [c*self.tile_size for c in wall[0]]
        end = [c*self.tile_size for c in wall[1]]
        pygame.draw.line(self.screen, (255,0,218), start, end)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--width", default=15, type=int, help="La larghezza della mappa")
    parser.add_argument("-a", "--height", default=15, type=int, help="L'altezza della mappa")
    parser.add_argument("-o", "--output", default="a.map", help="Il file di output")
    parser.add_argument("-i", "--input", default=None, help="Il file da editare")
    args = parser.parse_args()

    m = MapCreator((args.width,args.height), args.output, args.input)
    m.run()

if __name__ == '__main__':
    main()
