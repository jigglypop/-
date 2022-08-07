import sys
sys.stdin = open('./text/1298.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
words = 0
for _ in range(Int()):
    word = Str()
    error = 0
    for i in range(len(word) - 1):  
        if word[i] != word[i+1]:  
            _word = word[i + 1:]  
            if _word.count(word[i]) > 0: 
                error += 1  
    if error == 0:  
        words += 1 
print(words)