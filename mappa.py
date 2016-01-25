import line

class Mappa(object):
    def __init__(self):
        self.mappa = []

    def load(self, path):
        with open(path, "r") as map:
            for line in map:
                info = line.split(" ")
                self._parse(info)

    def get(self, posizione):
        return posizione in self.mappa

    def _parse(self, direttiva):
        istruzione = direttiva[0]
        if istruzione == 'l':
            self._parse_line(direttiva[1:])

    def _add_punto(self, posizione):
        self.mappa.append(posizione)

    def _parse_line(self, coord):
        start = (int(coord[0]), int(coord[1]))
        end = (int(coord[2]), int(coord[3]))
        res = line.gen_line(start, end)
        for punto in res:
            self._add_punto(punto)
