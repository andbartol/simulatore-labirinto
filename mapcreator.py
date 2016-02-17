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
        if input != None:
            with open(input, "rb") as f:
                self.map = pickle.load(f)
        else:
            self.map = [[self.isborder(x, y) for y in range(size[1])] for x in range(size[0])]

    def isborder(self, x, y):
        return 1 if x == 0 or y == 0 or x == self.size[0]-1 or y == self.size[1]-1 else 0

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

        with open("prova.map", "wb") as f:
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
        x = math.floor(event.pos[0]/self.tile_size)
        y = math.floor(event.pos[1]/self.tile_size)
        if event.buttons[0] == 1:
            self.add_tile((x,y))
        elif event.buttons[2] == 1:
            self.add_tile((x,y), 0)

    def add_tile(self, pos, value=1):
        try:
            self.map[pos[0]][pos[1]] = value
        except IndexError:
            pass

    def get_tile(self, pos):
        return self.map[pos[0]][pos[1]]

    def manage_keyboard(self, event):
        if event.key == pygame.K_ESCAPE:
            pygame.display.quit()
            self.exit = True

    def draw(self):
        self.screen.fill((0,0,0))
        self.draw_tiles()

    def draw_tiles(self):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                color = (255,0,218) if self.get_tile((x,y)) == 1 else (255,255,255)
                self.draw_tile(x, y, color)

    def draw_tile(self, x, y, color=(255,255,255)):
        pygame.draw.rect(self.screen, color, pygame.Rect(x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size))

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
