// 다익스트라

// const N = parseInt(input[0]);
// const M = parseInt(input[1]);

// const INF = Infinity;
// const dist = Array(N + 1).fill(INF);
// const graph = Array.from(Array(N + 1), () => Array());

// for (let i = 2; i < M + 2; i++) {
//   const [a, b, c] = input[i].split(" ").map(Number);
//   graph[a].push([c, b]);
// }
// const [A, B] = input[M + 2].split(" ").map(Number);

// const Q = [];
// Q.push([0, A]);
// dist[A] = 0;
// while (Q.length) {
//   let [cost, u] = Q.shift();
//   if (dist[u] < cost) continue;
//   for (let [w, v] of graph[u]) {
//     if (dist[v] > dist[u] + w) {
//       dist[v] = dist[u] + w;
//       Q.push([dist[v], v]);
//     }
//   }
// }
// console.log(dist[B]);

// 유니온 파인드

// const [n, m] = input[0];
// input.shift();
// parent = Array(n + 1)
//   .fill(0)
//   .map((_, i) => i);

// function find(x) {
//   if (parent[x] === x) {
//     return x;
//   } else {
//     let temp = find(parent[x]);
//     parent[x] = temp;
//     return temp;
//   }
// }

// function union(a, b) {
//   a = find(a);
//   b = find(b);
//   if (a !== b) {
//     parent[b] = a;
//   }
// }

// for (let i = 0; i < input.length; i++) {
//   const [a, b, c] = input[i];
//   if (a === 0) {
//     union(b, c);
//   } else {
//     if (find(b) === find(c)) {
//       console.log("YES");
//     } else {
//       console.log("NO");
//     }
//   }
// }

// 플로이드

// const floyd = (N, M, board) => {
//   const INF = Infinity;
//   const graph = Array.from(Array(N + 1), () => Array(N + 1).fill(INF));
//   for (let i = 0; i < M; i++) {
//     let [a, b, c] = board[i];
//     graph[a][b] = c;
//   }
//   for (let y = 1; y < N + 1; y++) {
//     for (let x = 1; x < N + 1; x++) {
//       if (y === x) {
//         graph[y][x] = 0;
//       }
//     }
//   }
//   for (let z = 1; z < N + 1; z++) {
//     for (let y = 1; y < N + 1; y++) {
//       for (let x = 1; x < N + 1; x++) {
//         graph[y][x] = Math.min(graph[y][x], graph[y][z] + graph[z][x]);
//       }
//     }
//   }
//   return graph;
// };
// console.log(
//   floyd(4, 7, [
//     [1, 2, 4],
//     [1, 4, 6],
//     [2, 1, 3],
//     [2, 3, 7],
//     [3, 1, 5],
//     [3, 4, 4],
//     [4, 3, 2],
//   ])
// );

// DFS

// const dfs = (sy, sx) => {
//   const visited = Array.from(Array(Y), () => Array(X).fill(false));
//   const di = [
//     [1, 0],
//     [-1, 0],
//     [0, 1],
//     [0, -1],
//   ];
//   const Q = [[sy, sx]];
//   board[sy][sx] = "2";
//   visited[sy][sx] = true;
//   while (Q.length) {
//     let [y, x] = Q.pop();
//     for (let [dy, dx] of di) {
//       let [ny, nx] = [y + dy, x + dx];
//       if (0 <= ny && ny < Y && 0 <= nx && nx < X) {
//         if (board[ny][nx] === "0" && !visited[ny][nx]) {
//           Q.push([ny, nx]);
//           visited[ny][nx] = true;
//           board[ny][nx] = "2";
//         }
//       }
//     }
//   }
// };

// BFS

// const bfs = (sy, sx) => {
//   const visited = Array.from(Array(Y), () => Array(X).fill(false));
//   const di = [
//     [1, 0],
//     [-1, 0],
//     [0, 1],
//     [0, -1],
//   ];
//   const Q = [[sy, sx]];
//   board[sy][sx] = "2";
//   visited[sy][sx] = true;
//   while (Q.length) {
//     let [y, x] = Q.shift();
//     for (let [dy, dx] of di) {
//       let [ny, nx] = [y + dy, x + dx];
//       if (0 <= ny && ny < Y && 0 <= nx && nx < X) {
//         if (board[ny][nx] === "0" && !visited[ny][nx]) {
//           Q.push([ny, nx]);
//           visited[ny][nx] = true;
//           board[ny][nx] = "2";
//         }
//       }
//     }
//   }
// };

function solution(num) {
  return fibo(num);
}
console.log(solution(3));
