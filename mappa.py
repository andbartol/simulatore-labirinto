import line

class Mappa(object):
    def __init__(self):
        self.linee = []

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

    def _parse_line(self, coord):
        start = (float(coord[0]), float(coord[1]))
        end = (float(coord[2]), float(coord[3]))
        self.linee.append((start,end))
