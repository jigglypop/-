import sys
sys.stdin = open('./text/1243.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

def isPalindrom(w) :
    if w: return w == w[::-1]
    else: return True

def go(dp, words, pre, w, l) :
    if not w:
        key = (True, "", l)
    else:
        key = (pre, w, l)
    if key not in dp:
        if l < 0 : return 0
        if l == 0 :
            dp[key] = 1 if isPalindrom(w) else 0
            return dp[key]
        board = []
        rw = w[::-1]

        def match(a, b) :
            if pre: return a.endswith(b)
            else: return a.startswith(b)

        def cut(a, b) :
            if not b:return a
            else:
                if pre: return a[:-len(b)]
                else: return a[len(b):]

        for w in words:
            if match(w, rw):
                board.append(go(dp, words, not pre, cut(w, rw), l - len(w)))
            elif match(rw, w) :
                board.append(go(dp, words, pre, cut(rw, w)[::-1], l - len(w)))
        dp[key] = sum(board)
    return dp[key]

def solve(words, L) :
    dp = {}
    return str(go(dp, words, True, "", L))

N = Int()
L = Int()
words = [Str() for _ in range(N)]
print(solve(words, L), end = '')