def gray_tone(color):
    data = color.lstrip('#')
    ldata = len(data)
    if ldata < 3:
        R = G = B = data
    elif ldata == 3:
        R, G, B = data
        R, G, B = R+R, G+G, B+B
    if ldata == 6:
        R, G, B = data[0:2], data[2:4], data[4:6]
    else:
        R, G, B = 255, 255, 255
    R, G, B = int(R, 16)/255, int(G, 16)/255, int(B, 16)/255
    L = 0.213*R + 0.715*G + 0.072*B
    return L
