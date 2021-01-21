// var input = require("fs").readFileSync("./dev/stdin").toString().trim().split("\n");

const input = require("fs").readFileSync("./2252.txt").toString().split("\r\n");

const [N, M] = input[0].split(" ").map(Number);
const tree = Array.from(Array(N + 1), () => Array());
const check = Array(N + 1).fill(0);

for (let i = 1; i < M + 1; i++) {
  const [a, b] = input[i].split(" ").map(Number);
  tree[a].push(b);
  check[b]++;
}

const Q = [];
for (let i = 1; i < N + 1; i++) {
  if (check[i] === 0) Q.push(i);
}
const result = [];
while (Q.length) {
  let u = Q.shift();
  resultA.push(u);
  for (let v of tree[u]) {
    check[v]--;
    if (check[v] === 0) {
      Q.push(v);
    }
  }
  result.push(u);
}
console.log(result.join(" "));
