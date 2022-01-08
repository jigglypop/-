def isPalindrome(word):
    for i in range(0, len(word) // 2):
        if word[i] != word[len(word) - 1 - i]:
            return False
    return True

def solution(P):
    ans = []
    N = len(P)
    _graph = [set() for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            word = P[i] + P[j]
            if isPalindrome(word):
                _graph[i].add(j)
                _graph[j].add(i)

    _graph = list(map(list, _graph))

    def matching(graph):
        total = 0
        pred = [-1 for _ in range(N + 1)]
        def dfs(u):
            if not check[u]:
                check[u] = True
                for v in graph[u]:
                    if pred[v] == -1 or dfs(pred[v]):
                        pred[v] = u
                        return True
                return False

        for i in range(N + 1):
            check = [False for _ in range(N + 1)]
            if dfs(i):
                total += 1
        if total + 2 == N:
            return True
        else:
            return False 

    if len(_graph[0]) == 1:
        return [P[_graph[0][0]]]
    result = []
    for i in sorted(_graph[0]):
        graph = []
        for g in _graph[1:]:
            temp = []
            for j in g:
                if j != i and j != 0:
                    temp.append(j)
            graph.append(temp)
        graph = [[]] + graph
        if matching(graph):
            result.append(P[i])
    return result

print(solution(["11","111","11","211"]))
print(solution(["21","123","111","11"]))
