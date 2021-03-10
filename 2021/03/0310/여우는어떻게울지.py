import sys
sys.stdin = open('9536.txt', 'r')
T = int(input())
for _ in range(T):
    words = input()
    words = words.split(" ")
    while True:
        temp = input()
        if temp == "what does the fox say?":
            break
        temp = temp.split(" ")[-1]
        _words = []
        for word in words:
            if word == temp:
                continue
            _words.append(word)
        words = _words
    print(*words)
