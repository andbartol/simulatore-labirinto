import program

class ProgramFinal(program.Program):
    def __init__(self):
        self.direction = 0
        self.back_left = False
        self.back_right = False

    def next_step(self, sens):

        if self.back_left:
            self.back_left = False
            if not sens[3]:
                return 3
            elif not sens[0]:
                return 0

        if self.back_right:
            self.back_right = False
            if not sens[1]:
                return 1
            elif not sens[0]:
                return 0

        if not sens[0]:
            return 0
        if not sens[3]:
            self.back_left = True #Deve tornare indietro e fare la prossima fila
            return 3
        if not sens[1]:
            self.back_right = True
            return 1
        return 2
