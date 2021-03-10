import sys
sys.stdin = open("1251.txt", "r")
words = input()
word_list = []
for i in range(1, len(words)):
    for j in range(i+1, len(words)):
        A = words[:i][::-1]
        B = words[i:j][::-1]
        C = words[j:][::-1]
        word_list.append(A + B + C)
word_list.sort()
print(word_list[0])
