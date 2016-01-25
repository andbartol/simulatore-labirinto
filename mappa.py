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

    def _gen_line(self, start, end):
        # Setup initial conditions
        x1, y1 = start
        x2, y2 = end
        dx = x2 - x1
        dy = y2 - y1

        # Determine how steep the line is
        is_steep = abs(dy) > abs(dx)

        # Rotate line
        if is_steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        # Swap start and end points if necessary and store swap state
        swapped = False
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            swapped = True
        # Recalculate differentials
        dx = x2 - x1
        dy = y2 - y1
        # Calculate error
        error = int(dx / 2.0)
        ystep = 1 if y1 < y2 else -1
        # Iterate over bounding box generating points between start and end
        y = y1
        points = []
        for x in range(x1, x2 + 1):
            coord = (y, x) if is_steep else (x, y)
            points.append(coord)
            error -= abs(dy)
            if error < 0:
                y += ystep
                error += dx
        # Reverse the list if the coordinates were swapped
        if swapped:
            points.reverse()
        return points
