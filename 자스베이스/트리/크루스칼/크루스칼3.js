let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin", "utf8").split("\n");
let input = fs.readFileSync("./1922.txt", "utf8").split("\r\n");
let idx = 0;
const V = parseInt(input[idx++]);
const E = parseInt(input[idx++]);

let parent = new Array(V + 1).fill(0).map((_, i) => i);
let edges = [];
for (let i = 0; i < E; i++) {
  let [a, b, cost] = input[idx++].split(" ").map(Number);
  edges.push({ cost: cost, a: a, b: b });
}
edges.sort((a, b) => a.cost - b.cost);

let result = 0;
const find = (x) => {
  if (parent[x] === x) return x;
  return (parent[x] = find(parent[x]));
};

const union = (_a, _b) => {
  let a = find(_a);
  let b = find(_b);
  parent[a] = b;
};

for (let edge of edges) {
  if (find(edge.a) !== find(edge.b)) {
    union(edge.a, edge.b);
    result += edge.cost;
  }
}
console.log(result);
