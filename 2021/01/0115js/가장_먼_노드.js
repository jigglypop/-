function solution(n, edge) {
  var tree = Array.from(Array(n + 1), () => Array());
  for (let [a, b] of edge) {
    tree[a].push(b);
    tree[b].push(a);
  }
  var dist = Array(n + 1).fill(0);
  dist[1] = 1;
  let Q = [1];
  while (Q.length) {
    let u = Q.shift();
    for (let v of tree[u]) {
      if (dist[v] === 0) {
        dist[v] = dist[u] + 1;
        Q.push(v);
      }
    }
  }
  dist = dist.slice(1, dist.length);
  const Max = Math.max(...dist);
  return dist.reduce((acc, cur) => (cur === Max ? (acc += 1) : (acc += 0)), 0);
}
console.log(
  solution(6, [
    [3, 6],
    [4, 3],
    [3, 2],
    [1, 3],
    [1, 2],
    [2, 4],
    [5, 2],
  ])
);
