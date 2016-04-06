import program

class ProgramAsk(program.Program):
    def next_step(self, sens):
        print(sens)
        return int(input("Scegli una direzione -> "))
