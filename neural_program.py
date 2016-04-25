import program
from neat import nn, parallel, population, visualize
import sys

class NeuralProgram(program.Program):
    def __init__(self, net):
        self.net = net

    def next_step(self, sens):
        s = [1 if x else -1 for x in sens]
        out = self.net.activate(s)
        return out.index(max(out))
