import sys
sys.stdin = open('16968.txt', 'r')

input = sys.stdin.readline
alpha = str(input())
alpha_dict = {'c': 26, 'd': 10}
start = 26 if alpha[0] == 'c' else 10
for i in range(1, len(alpha)):
    if alpha[i] == alpha[i-1]:
        start *= alpha_dict[alpha[i]] - 1
    else:
        start *= alpha_dict[alpha[i]]
print(start)
