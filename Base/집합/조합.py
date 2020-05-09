import pprint


def combinations(arr,r):
    R = []
    def comb(k,start,chosen):
        if k == r:
            copy = chosen[::]
            R.append(copy)
            return
        for i in range(start,len(arr)):
            chosen.append(arr[i])
            comb(k+1,i+1,chosen)
            chosen.pop()
    comb(0,0,[])
    return R

pprint.pprint(combinations('ABCDE', 2))
