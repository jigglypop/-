// var input = require("fs")
//   .readFileSync("./dev/stdin")
//   .toString()
//   .trim()
//   .split("\n");

const input = require("fs").readFileSync("./1916.txt").toString().split("\r\n");

const N = parseInt(input[0]);
const M = parseInt(input[1]);

const INF = Infinity;
const dist = Array(N + 1).fill(INF);
const graph = Array.from(Array(N + 1), () => Array());

for (let i = 2; i < M + 2; i++) {
  const [a, b, c] = input[i].split(" ").map(Number);
  graph[a].push([c, b]);
}
const [A, B] = input[M + 2].split(" ").map(Number);

const Q = [];
Q.push([0, A]);
dist[A] = 0;
while (Q.length) {
  let [cost, u] = Q.shift();
  if (dist[u] < cost) continue;
  for (let [w, v] of graph[u]) {
    if (dist[v] > dist[u] + w) {
      dist[v] = dist[u] + w;
      Q.push([dist[v], v]);
    }
  }
}
console.log(dist[B]);
