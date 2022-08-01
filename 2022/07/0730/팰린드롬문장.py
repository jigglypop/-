from itertools import combinations
import sys
sys.stdin = open('./text/1054.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

def isPalindrom(w) :
    return w == w[::-1]

def goA(dpA, dpB, p, s, words) :
    key = (p, s, frozenset(words))
    if key not in dpB:
        if p is not None:
            if not words:
                dpB[key] = 1 if isPalindrom(p) else 0
                return dpB[key]
            board = []
            rp = p[::-1]
            if rp in words:
                board.append(goB(dpA, dpB, words - set([rp])))
            dpB[key] = sum(board + [goA(dpA, dpB, None, w[:-len(p)], words-set([w])) for w in [w for w in words-set([rp]) if w.endswith(rp)]] + [goA(dpA, dpB, p[len(w):], None, words-set([w])) for w in [w for w in words-set([rp]) if rp.endswith(w)]])
            return dpB[key]

        if s is not None:
            if not words:
                dpB[key] = 1 if isPalindrom(s) else 0
                return dpB[key]
            board = []
            rs = s[::-1]
            if rs in words:
                board.append(goB(dpA, dpB, words-set([rs])))
            dpB[key] = sum(board + [goA(dpA, dpB, w[len(s):], None, words-set([w])) for w in [w for w in words-set([rs]) if w.startswith(rs)]] + [goA(dpA, dpB, None, s[:-len(w)], words-set([w])) for w in [w for w in words-set([rs]) if rs.startswith(w)]])
            return dpB[key]
    return dpB[key]

def goB(dpA, dpB, words) :
    key = frozenset(words)
    if key not in dpA:
        if not words: dpA[key] = 1
        else: dpA[key] = sum([goA(dpA, dpB, w, None, words-set([w])) for w in words])
    return dpA[key]

def solve(words):
    dpA = {}
    dpB = {}
    return str(sum([goB(dpA, dpB, set(_words)) for L in range(1, len(words) + 1) for _words in combinations(words, L)]))

N = Int()
words = [i for i in [Str() for _ in range(N)] if i]
print(solve(words), end='')