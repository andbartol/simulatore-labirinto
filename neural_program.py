import program
from neat import nn, parallel, population, visualize
import sys

class NeuralProgram(program.Program):
    def __init__(self, net):
        self.net = net

    def next_step(self, sens):
        s = [int(x) for x in sens]
        out = self.net.activate(s)
        return out.index(max(out))
