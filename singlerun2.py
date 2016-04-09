import argparse
import maputilities
import math
import pickle
import robot2
import program
import neural_program
import ProgramAsk
import copy
import sys

from neat import nn, parallel, population

class SingleRun():
    def __init__(self, map, program, position=[0,0], max_turns=30):
        self.map = map
        self.robot = robot2.Robot2(self.map, position)
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
    with open(sys.argv[1], "rb") as f:
        genome = pickle.load(f)
    pheno = nn.create_feed_forward_phenotype(genome)
    p = neural_program.NeuralProgram(pheno)
    s = SingleRun(map, p)
    s.play()
    print(s.points)

if __name__ == '__main__':
    main()
