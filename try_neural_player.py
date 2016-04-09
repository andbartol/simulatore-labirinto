import neural_program_try
from neat import nn, parallel, population, visualize
import pickle
import argparse
import sys
import singlerun2

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", default="res_0.net", help="Il file con la rete da aprire")
    parser.add_argument("-m", "--map", default="prova.map", help="La mappa da usare")
    args = parser.parse_args()

    with open(args.input, "rb") as f:
        genome = pickle.load(f)

    with open(args.map, "rb") as f:
        map = pickle.load(f)
    net = nn.create_feed_forward_phenotype(genome)
    prog = neural_program_try.NeuralProgram(net)
    s = singlerun2.SingleRun(map, prog)
    print(s.play())

if __name__ == '__main__':
    main()
