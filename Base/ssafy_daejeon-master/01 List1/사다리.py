import pprint

def D(sy,sx):
    m[sy][sx] = 0
    if sy == 0:
        return sx
    elif m[sy][sx-1] == 1:
        print(sy,sx-1)        
        return D(sy,sx-1)
    elif m[sy][sx+1] == 1:
        print(sy,sx+1)
        return D(sy,sx + 1)
    else:
        print(sy-1,sx)
        return D(sy -1, sx)

m = [[0,1,0,1,0,1,0],
     [0,1,1,1,0,1,0],
     [0,1,0,1,0,1,0],
     [0,1,0,1,1,1,0],
     [0,1,0,1,0,1,0],
     [0,1,0,1,1,1,0],
     [0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0],
     [0,1,0,2,0,1,0],
     [0,0,0,0,0,0,0]]

print(D(9,3))
pprint.pprint(m)