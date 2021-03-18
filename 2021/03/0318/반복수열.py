import sys
sys.stdin = open("2331.txt", "r")
A, P = map(int, input().split())
S = [A]
set_s = set()
set_s.add(A)
break_number = -1
while True:
    top = S[-1]
    _next = sum(list(map(lambda x: x ** P, list(map(int, str(top))))))
    if _next in set_s:
        break_number = _next
        break
    S.append(_next)
    set_s.add(_next)
print(S)
print(len(S[:S.index(break_number)]))
