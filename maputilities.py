def is_inner(wall, map, dimensions, previouses):
    return not is_outer(wall, map, dimensions, previouses)

def is_outer_block(position, map, dimensions):
    w = []
    w.append([[position[0], position[1]], [position[0]+1, position[1]]])
    w.append([[position[0]+1, position[1]], [position[0]+1, position[1]+1]])
    w.append([[position[0], position[1]+1], [position[0]+1, position[1]+1]])
    w.append([[position[0], position[1]], [position[0], position[1]+1]])
    outer = False
    for i in w:
        if i in map or invert_wall(i) in map:
            outer = outer or is_outer(i, map, dimensions, [])
    return outer

def is_inner_block(position, map, dimensions):
    return not is_outer_block(position, map, dimensions)

def is_outer(wall, map, dimensions, previouses):
    """
    Controlla se un muro è deve essere contato come muro esterno o interno
    Controlla ricorsivamente i vicini fino ad arrivare ad un muro senza vicini,
    poi controlla se il muro è un muro esterno

    previouses deve essere []
    """
    vicini = trova_vicini(wall, dimensions, previouses)
    for vicino in vicini:
        if vicino in map or invert_wall(vicino) in map:
            previouses.append(wall)
            #C'è un vicino segnato come muro esterno?
            if is_outer(vicino, map, dimensions, previouses):
                return True
    #Non è stato trovato un muro già marcato come esterno
    return is_fuori(wall, dimensions)

def trova_vicini(wall, dimensions, previouses):
    """
    Trova tutti i possibili vicini ad un muro, poi toglie quelli gia presi in considerazione
    """
    x1 = wall[0][0]
    y1 = wall[0][1]
    x2 = wall[1][0]
    y2 = wall[1][1]

    """
    Genera tutti i vicini possibili
    """
    neigh = []
    neigh.append([[x1,y1],[x1,y1+1]])
    neigh.append([[x1,y1],[x1,y1-1]])
    neigh.append([[x1,y1],[x1-1,y1]])
    neigh.append([[x1,y1],[x1+1,y1]])

    neigh.append([[x2,y2],[x2,y2+1]])
    neigh.append([[x2,y2],[x2,y2-1]])
    neigh.append([[x2,y2],[x2-1,y2]])
    neigh.append([[x2,y2],[x2+1,y2]])

    #rimuove il muro stesso
    if wall in neigh:
        neigh.remove(wall)
    if invert_wall(wall) in neigh:
        neigh.remove(invert_wall(wall))

    #rimuove i vicini gia visitati
    for prev in previouses:
        if prev in neigh:
            neigh.remove(prev)
        if prev and (invert_wall(prev) in neigh):
            neigh.remove(invert_wall(prev))

    return neigh

def invert_wall(wall):
    n_wall = []
    n_wall.append(wall[1])
    n_wall.append(wall[0])
    return n_wall

def is_fuori(wall, dimensions):
    """
    Controlla se un muro è nel bordo
    """
    x1 = wall[0][0]
    y1 = wall[0][1]
    x2 = wall[1][0]
    y2 = wall[1][1]

    left = x1 == x2 == 0
    right = x1 == x2 == dimensions[0]

    up = y1 == y2 == 0
    down = y1 == y2 == dimensions[1]

    return left or right or up or down

def is_horizontal(wall):
    return wall[0][1] == wall[1][1]

def is_vertical(wall):
    return not is_horizontal(wall)
