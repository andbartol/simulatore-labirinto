import argparse
import maputilities
import math
import pickle
import robot2
import program
import ProgramAsk
import copy
import sys

class SingleRun():
    def __init__(self, map, program, max_turns=30):
        self.map = map
        self.robot = robot2.Robot2(self.map)
        self.program = program
        self.passed = []
        self.points = 0
        self.max_turns = max_turns

    def step(self):
        sense = self.robot.sense()
        direction = self.program.next_step(sense)
        self.robot.move(direction)

    def update_points(self):
        if not self.robot.position in self.passed:
            self.passed.append(copy.copy(self.robot.position))
            if maputilities.is_outer_block(self.robot.position, self.map, [15,15]):
                points = 1
            else:
                points = 2
            self.points += points

    def play(self):
        for turn in range(self.max_turns):
            self.step()
            self.update_points()
        return self.points

def main():
    with open("prova.map", "rb") as f:
        map = pickle.load(f)
        p = ProgramAsk.ProgramAsk()
        s = SingleRun(map, p)
        s.play()
        print(s.points)

if __name__ == '__main__':
    main()
