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

# 나머지 정리

1) (A+B)%C =((A%C) + (B%C))%C

2) (A*B)%C =((A%C) *(B%C))%C