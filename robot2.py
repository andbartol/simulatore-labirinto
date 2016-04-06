import maputilities

class Robot2():
    def __init__(self, map, position=[0,0]):
        self.map = map
        self.position = position

    def sense(self):
        """
        Ritorna un array con l'indicazione se c'è un muro
        per ogni sensore
        """
        sens = [False for x in range(4)]
        #Solo i muri con una coordinata in comune con la posizione
        for wall in filter((lambda x: x[0] == self.position or x[1] == self.position), self.map):
            if wall[0] == self.position:
                if maputilities.is_horizontal(wall):
                    if wall[1][0] > wall[0][0]:
                        sens[0] = True
                else:
                    if wall[1][1] > wall[0][1]:
                        sens[3] = True
            else:
                if maputilities.is_horizontal(wall):
                    if wall[0][0] > wall[1][0]:
                        sens[0] = True
                else:
                    if wall[0][1] > wall[1][1]:
                        sens[3] = True

        pos = []
        pos.append(self.position[0]+1)
        pos.append(self.position[1]+1)
        for wall in filter((lambda x: x[0] == pos or x[1] == pos), self.map):
            if wall[0] == pos:
                if maputilities.is_horizontal(wall):
                    if wall[1][0] < wall[0][0]:
                        sens[2] = True
                else:
                    if wall[1][1] < wall[0][1]:
                        sens[1] = True
            else:
                if maputilities.is_horizontal(wall):
                    if wall[0][0] < wall[1][0]:
                        sens[2] = True
                else:
                    if wall[0][1] < wall[1][1]:
                        sens[1] = True
        return sens

    def move(self, direction):
        """
        Prova a muoversi in una direzione
        """
        sense = self.sense()
        if not sense[direction]: #Se non stiamo andando contro un muro
            if direction == 0:
                self.position[1] -= 1
            elif direction == 1:
                self.position[0] += 1
            elif direction == 2:
                self.position[1] += 1
            elif direction == 3:
                self.position[0] -= 1
