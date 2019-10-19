#game.map
#by boot1110001

def crete_base_map(vsqW, vsqH):
    out = []
    i = 0
    while i < vsqH:
        out.append([])
        e = 0
        while e < vsqW:
            out[i].append(0)
            e += 1
        i += 1
    return out
