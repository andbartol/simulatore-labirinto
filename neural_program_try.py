import program
from neat import nn, parallel, population, visualize
import sys

class NeuralProgram(program.Program):
    def __init__(self, net):
        self.net = net

    def next_step(self, sens):
        out = self.net.serial_activate(sens)
        r = out.index(max(out))
        print(r)
        return r
