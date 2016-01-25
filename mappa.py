import line

class Mappa(object):
    def __init__(self, dimensione):
        self.dimensione = dimensione
        self.mappa = [[False for y in range(dimensione[1])] for x in range(dimensione[0])]

    def load(self, path):
        with open(path, "r") as map:
            line = map.readline()
            line = line.split(" ")
            self._parse(line)

    def get(self, posizione):
        return self.mappa[posizione[0]][posizione[1]]

    def _parse(self, direttiva):
        istruzione = direttiva[0]
        if istruzione == 'l':
            self._parse_line(direttiva[1:])

    def _add_punto(self, posizione):
        self.mappa[posizione[0]][posizione[1]] = True

    def _parse_line(self, coord):
        start = (int(coord[0]), int(coord[1]))
        end = (int(coord[2]), int(coord[3]))
        res = line.gen_line(start, end)
        for punto in res:
            self._add_punto(punto)
