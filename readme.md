# 배열조작

```python
board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

di = [(-1, -1), (-1, 0), (-1, 1),
      (0, -1), (0, 0), (0, 1),
      (1, -1), (1, 0), (1, 1)]
"""
-1-1-1
0 0 0 
1 1 1

-1 0 1
-1 0 1
-1 0 1
"""
```

# 배열회전

```python
# 90도 한줄
rotated = list(zip(*reversed(arr)))

# 90도
one = [[0] * 3 for _ in range(3)]
for y in range(N):
    for x in range(N):
        one[x][N-1-y] = arr[y][x]
# 180도
two = [[0] * 3 for _ in range(3)]
for y in range(N):
    for x in range(N):
        two[N-1-y][N-1-x] = arr[y][x]
# 270도
three = [[0] * 3 for _ in range(3)]
for y in range(N):
    for x in range(N):
        three[N-1-x][y] = arr[y][x]
# 전치행렬
four = [[0] * 3 for _ in range(3)]
for y in range(N):
    for x in range(N):
        four[x][y] = arr[y][x]
```



# 정규 표현식 (Regular Expressions)

------

## 메타 문자 (Meta Characters)

- 정규식에서 사용하는 특별한 의미를 지니는 문자

### 문자 클래스 [ ]

- [ ]사이의 문자들과의 일치성을 확인
  ex1) [abc] -> 'and'이면 'a'가 있으므로 매치
  ex2) [abc] -> 'hello'이면 일치하는것이 없으므로 매치 X

- [i-j] '-'는 두 문자 사이 범위를 나타냄
  ex) [a-zA-Z] = 알파벳 대, 소문자 모두와의 매치 확인

- '^'를 사용하여 not의 의미를 나타냄

  ex) [^a-zA-Z] = 알파벳 대, 소문자가 아닌 문자와의 매치 확인

  > <자주 사용하는 문자 클래스>
  > \d = [0-9]
  > \D = [^0-9]
  > \s = [ \t\n\r\f\v] -> whitespace문자와 매치
  > \S = [^ \t\n\r\f\v]
  > \w = [a-zA-Z0-9]
  > \W = [^a-zA-Z0-9]

### Dot(.)

- \n을 제외한 모든 문자와 매치
  ex) a.b = a + 모든문자 + b -> abc와는 매치X

### 반복(*) & (+)

- '*****'의 바로 앞 문자가 0번 이상 반복되어 매치되는지 확인
  ex) do*g -> dg, dog, dooog 모두 매치O
- '+'의 바로 앞 문자가 1번 이상 반복되어 매치되는지 확인
  ex) do*g -> dg 매치 X, dog, dooog 매치O

### 반복 ({m, n}, ?)

- 반복 횟수를 설정할 때 사용
- m, n은 생략가능
- {m} = m번만 반복
  ex) do{2}g -> dog 매치 X, doog 매치 O, doooog 매치 X
- {m, n} = m~n회 반복
  ex) do{1, 3}g -> doooooog 매치 X
- ? = {0, 1} = ?앞 문자가 있어도 되고 없어도 됨
  ex) do?g -> dg, dog, doog 매치 O

## Python re 모듈 사용

- 조건에 맞을 경우 해당 모듈의 객체 반환
- 맞지 않을 경우 None 반환

### match

- 처음부터 매치되는지 확인

```python
import re

# 비밀번호 검정 함수
def password_validation_check(pwd_signin):
    p = re.compile('\S')

    pw = p.match(pwd_signin) # 조건에 맞을 경우 match객체 반환

    if pw:
        return True
    else:
        return False
```

### search

- 전체에서 매치되는지 확인

```python
p = re.compile('[a-z]+')

m = p.search('25abc') # 객체 반환
```

### findall

- 매치해서 리스트로 돌려줌

```python
m = p.findall('My dream was to be a pilot')
print(m)

# ['My', 'dream', 'was', 'to', 'be', 'a', 'pilot']
```

### match 객체 메소드

```python
m = p.match('pyhon')

m.group() # 'python'

m.start() # 0

m.end() # 6

m.span() # (0, 6) -> tuple
```

- 're.I' : 대소문자 관계없이 매치

- 're.M' : 여러 줄과 매치




# 위상 정렬(DAG)

```python
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
check = [0 for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[A].append(B)
    check[A] += 1
Q = deque()
for i in range(1, N+1):
    if check[i] == 0:
        Q.append(i)
while Q:
    u = Q.popleft()
    for v in graph[u]:
        check[v] -= 1
        if check[v] == 0:
            Q.append(v)
    print(u, end=" ")
```



# 다익스트라

---

```python
V, E = map(int, input().split())
start = int(input())
graph = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
dist = defaultdict(int)
Q = [(0, start)]
while Q:
    time, node = heappop(Q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = time + w
            heappush(Q, (alt, v))
print(dist)
print(graph)

```

# 유니온 파인드

```python
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b
```

# 크루스칼

```python
V, E = map(int, input().split())
parent = [i for i in range(V+1)]

edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))
edges.sort()
result = 0

for C, A, B in edges:
    if find(parent, A) != find(parent, B):
        union(parent, A, B)
        result += C
print(result)
```

# 프림

```python
from collections import deque
import heapq
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

heap = []
visited[1] = True
result = 0
cnt = 1
for a in graph[1]:
    heapq.heappush(heap, a)
while heap:
    cost, to = heapq.heappop(heap)
    if not visited[to]:
        visited[to] = True
        cnt += 1
        result += cost
        for u in graph[to]:
            heapq.heappush(heap, u)
    if cnt == V:
        break
print(result)

```

# 플로이드 

```python
import sys
INF = sys.maxsize
N, M = map(int, input().split())
graph = [[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c, = map(int, input().split())
    graph[a][b] = c

for y in range(1, N+1):
    for x in range(1, N+1):
        if y == x:
            graph[y][x] = 0

for z in range(1, N+1):
    for y in range(1, N+1):
        for x in range(1, N+1):
            graph[y][x] = min(graph[y][x], graph[y][z] + graph[z][x])

for y in range(1, N+1):
    print(graph[y][1:])

```





# 나머지 정리

1) (A+B)%C =((A%C) + (B%C))%C

2) (A*B)%C =((A%C) *(B%C))%C



# DP(LIS)

```
N = int(input())
S = [0] + list(map(int, input().split()))
DP = [0] * (N+1)
DP[1] = 1
for i in range(2, N+1):
    for j in range(1, i):
        if S[i] > S[j]:
            DP[i] = max(DP[j], DP[i])
    DP[i] += 1
print(max(DP))
```



# TOP DOWN

```python
import sys
sys.setrecursionlimit(2000*2000)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if DP[n] != -1:
        return DP[n]
    DP[n] = fibonacci(n-1) + fibonacci(n-2)
    return DP[n]
n = int(input())
DP = [-1] * (n+1)
fibonacci(n)
print(DP[n])
```



# BOTTOM UP

```python
def fibonacci(n):
    DP[0] = 0
    DP[1] = 1
    for i in range(2, n+1):
        DP[i] = DP[i-1] + DP[i-2]
n = int(input())
DP = [-1] * (n+1)
fibonacci(n)
print(DP[n])
```



# KMP

```python
def LPS(pat, lps):
    leng = 0
    i = 1
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1

def KMP(pat, txt):
    M = len(pat)
    N = len(txt)
    lps = [0]*M
    LPS(pat, lps)
    i = 0  # index for txt[]
    j = 0  # index for pat[]
    while i < N:
        if txt[i] == pat[j]:
            i += 1
            j += 1
        elif txt[i] != pat[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == M:
            print("Found pattern at index " + str(i-j))
            j = lps[j-1]

txt = 'ABXABABXAB'
pat = 'ABXAB'
KMP(pat, txt)
```

# 트라이

```python
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode)

    def __repr__(self):
        return f'TrieNode({self.word}:{self.children.items()})'


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

trie = Trie()
trie.insert('apple')
trie.insert('appeal')
print(trie.search('apple'))
```



# 순열

```python
def PERM(arr, r):
    result = []

    def perm(k, choice, used):
        if k == r:
            result.append(choice[::])
            return
        for i in range(len(arr)):
            if used & (1 << i):
                continue
            choice.append(arr[i])
            perm(k+1, choice, used | (1 << i))
            choice.pop()

    perm(0, [], 0)
    return result


result = PERM('ABC', 2)
```

```python
def PERM(arr, r):
    result = []
    def perm(arr, r):
        for i in range(len(arr)):
            if r == 1:
                yield [arr[i]]
            else:
                for next in perm(arr[:i] + arr[i+1:], r-1):
                    yield [arr[i]] + next
    for i in perm(arr, r):
        result.append(i)
    return result
 

result = PERM('ABCDE', 2)
```

# 조합

```python
def COMB(arr, r):
    result = []

    def comb(k, chosen, start):
        if k == r:
            result.append(chosen[::])
            return
        for i in range(start, len(arr)):
            chosen.append(arr[i])
            comb(k+1, chosen, i+1)
            chosen.pop()
    comb(0, [], 0)
    return result

result = COMB('ABCDE', 2)
```

```python
def COMB(arr, r):
    result = []
    def comb(arr, r):
        for i in range(len(arr)):
            if r == 1:
                yield [arr[i]]
            else:
                for next in comb(arr[i+1:], r-1):
                    yield [arr[i]] + next
    for i in comb(arr, r):
        result.append(i)
    return result

result = COMB('ABCDE', 2)
```

