N = 4
bit = [0] * N

for i in range(2):
    bit[0] = i
    for i in range(2):
        bit[1] = i
        for i in range(2):
            bit[2] = i
            for i in range(2):
                bit[3] = i
                print(bit)

# arr = 'ABC'
# bits = [0]*3

# for i in range(2):
#     bits[0] = i
#     for i in range(2):
#         bits[1] = i
#         for i in range(2):
#             bits[2] = i
#             print(bits,end='> ')
#             for i in range(len(bits)):
#                 if bits[i]: 
#                     print(arr[i],end='')
#             print()



# def subset(k,n):    
#         if k == n:
#             print(bits, end='> ')
#             for i in range(len(bits)):
#                 if bits[i]:print(arr[i], end='')
#             print()
#             return 

#         for i in range(2):
#             bits[k] = 0
#             subset(k+1,n)