"""
Usa la libreria neat
http://neat-python.readthedocs.org/en/latest/installation.html#from-source-using-setup-py
git clone https://github.com/CodeReclaimers/neat-python.git
python setup.py install
"""

from __future__ import print_function

import math
import os
import time
import pickle
import singlerun2
import neural_program

from neat import nn, parallel, population

def fitness(genome):
    net = nn.create_feed_forward_phenotype(genome)

    with open("prova.map","rb") as f:
        map = pickle.load(f)
    program = neural_program.NeuralProgram(net)
    s = singlerun2.SingleRun(map, program)
    return s.play()


def run():

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'lab_config')

    pe = parallel.ParallelEvaluator(9, fitness)

    pop = population.Population(config_path)
    for i in range(20):
        pop.run(pe.evaluate, 1)
        winner = pop.statistics.best_genome()

        with open("res_%d.net" % i, "wb") as f:
            pickle.dump(winner, f)

if __name__ == '__main__':
    run()
