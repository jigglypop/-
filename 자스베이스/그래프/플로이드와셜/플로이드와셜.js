const floyd = (N, M, board) => {
  const INF = Infinity;
  const graph = Array.from(Array(N + 1), () => Array(N + 1).fill(INF));
  for (let i = 0; i < M; i++) {
    let [a, b, c] = board[i];
    graph[a][b] = c;
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
  return graph;
};
console.log(
  floyd(4, 7, [
    [1, 2, 4],
    [1, 4, 6],
    [2, 1, 3],
    [2, 3, 7],
    [3, 1, 5],
    [3, 4, 4],
    [4, 3, 2],
  ])
);
