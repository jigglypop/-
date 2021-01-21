function solution(n, costs) {
  var parent = Array(n + 1)
    .fill(0)
    .map((_, i) => i);

  var edges = [];
  for (let [a, b, cost] of costs) {
    edges.push([cost, a, b]);
  }
  edges.sort((a, b) => a[0] - b[0]);
  let result = 0;

  const union = (_a, _b) => {
    var a = find(_a);
    var b = find(_b);
    parent[a] = b;
  };

  const find = (x) => {
    if (parent[x] === x) return x;
    return (parent[x] = find(parent[x]));
  };
  for (let [cost, a, b] of edges) {
    if (find(a) !== find(b)) {
      union(a, b);
      result += cost;
    }
  }
  return result;
}
console.log(
  solution(4, [
    [0, 1, 1],
    [0, 2, 2],
    [1, 2, 5],
    [1, 3, 1],
    [2, 3, 8],
  ])
);
