function solution(N, roads, K) {
  var answer = 0;
  const INF = Infinity;
  const graph = Array.from(Array(N + 1), () => Array(N + 1).fill(INF));
  for (let road of roads) {
    [a, b, c] = road;
    graph[a][b] = Math.min(graph[a][b], c);
    graph[b][a] = Math.min(graph[b][a], c);
  }
  for (let y = 1; y < N + 1; y++) {
    for (let x = 1; x < N + 1; x++) {
      if (y === x) {
        graph[y][x] = 0;
      }
    }
  }
  for (let z = 1; z < N + 1; z++) {
    for (let y = 1; y < N + 1; y++) {
      for (let x = 1; x < N + 1; x++) {
        graph[y][x] = Math.min(graph[y][x], graph[y][z] + graph[z][x]);
      }
    }
  }
  let results = graph[1];
  for (let result of results) {
    if (result <= K) answer++;
  }
  return answer;
}
console.log(
  solution(
    5,
    [
      [1, 2, 1],
      [2, 3, 3],
      [5, 2, 2],
      [1, 4, 2],
      [5, 3, 1],
      [5, 4, 2],
    ],
    3
  )
);
