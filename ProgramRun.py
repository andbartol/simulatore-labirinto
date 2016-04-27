import RoboSerial
import neural_program
import ProgramFinal
from neat import nn, parallel, population

BLACK_THRESHOLD = 320

def main():
    rs = RoboSerial.RoboSerial()
    # with open(sys.argv[1], "rb") as f:
        # genome = pickle.load(f)
    # pheno = nn.create_feed_forward_phenotype(genome)
    # p = neural_program.NeuralProgram(pheno)
    p = ProgramFinal.ProgramFinal(rs)

    while True:
        sens = readSens(rs)
        command = p.next_step(sens)
        if sens[5]:
            rs.leaveRescuePack()
        parseCommand(command, rs)

def readSens(rs):
    '''
    INPUT
            3
     ______________
    |              |
    |              |
  4 |              |  2
    |              |
    |              |
    |              |
  5 |              |  1
    |              |
    |              |
    |______________|

    OUTPUT
        0

    3       1

        2

    True: muro
    False: vuoto

    4 = True: nero
    '''
    sens = []
    for i in range(5):
        s = rs.requestSensor(i)
        if s >= 255:
            s = False
        else:
            s = True
        sens.append(s)
    s = []
    s.append(sens[2])
    s.append(sens[0] or sens[1])
    s.append(True)
    s.append(sens[3] or sens[4])

    color = rs.requestSensor(7)
    if color <= BLACK_THRESHOLD:
        color = True
    else:
        color = False
    s.append(color)
    temp = rs.requestSensor(8)
    if temp >= TEMP_THRESHOLD:
        temp = True
    else:
        temp = False
    s.append(temp)
    return s

def parseCommand(command, rs):
    if command == 1:
        rs.goRight()
    elif command == 3:
        rs.goLeft()
    elif command == 2:
        rs.goBack()
    forward(rs)

def forward(rs):
    old_dist = rs.requestSensor(10)
    while rs.requestSensor(10)-old_dist < 30:
        rs.goForward()

if __name__ == '__main__':
    main()
