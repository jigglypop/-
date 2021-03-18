import sys
sys.stdin = open("13273.txt", "r")
roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
number = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
rn = dict(zip(roman, number))
nr = dict(zip(number, roman))


def ntor(n):
    res = ''
    k = n
    nums = number[::-1]
    for i in range(len(nums)):
        while True:
            if nums[i] > k:
                break
            k -= nums[i]
            res += roman[::-1][i]
    return res


def rton(r, prev='M'):
    k = 0
    if not r:
        return 0
    elif r[0:2] in roman:
        k = 2
    elif r[0] in roman:
        k = 1
    if k:
        symb = r[0:k]
        prev = symb
        return number[roman.index(symb)] + rton(r[k:], symb)


for T in range(int(input())):
    n = input()
    if n.isdigit():
        print(ntor(int(n)))
    else:
        print(rton(n))
