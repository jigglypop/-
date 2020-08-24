import pprint

# def COMB(arr,r):
#     global R
#     chosen = []
#     def comb(k,start):
#         if k == r:
#             copy = chosen[::]
#             R.append(copy)
#             return
#         for i in range(start,len(arr)):
#             chosen.append(arr[i])
#             comb(k+1,i+1)
#             chosen.pop()
#     comb(0,0)
# R = []
# COMB('ABCDE',2)
# print(R)


def PERM(arr, r):
    global R
    used = [0 for _ in range(len(arr))]

    def perm(k, chosen, used):
        if k == r:
            copy = chosen[::]
            R.append(copy)
            return
        for i in range(len(arr)):
            chosen.append(arr[i])
            used[i] = 1
            perm(k+1, chosen, used)
            used[i] = 0
            chosen.pop()
    perm(0, [], used)


R = []
PERM('ABCDE', 2)
print(len(R))
