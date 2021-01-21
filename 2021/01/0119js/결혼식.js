// const input = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n");
const input = require("fs")
  .readFileSync("./5567.txt")
  .toString()
  .trim()
  .split("\n");
const n = parseInt(input[0]);
const m = parseInt(input[1]);
let tree = Array.from(Array(n + 1), () => Array());
let check = Array.from(Array(n + 1), () => 0);

for (let i = 2; i < m + 2; i++) {
  let [a, b] = input[i].split(" ").map(Number);
  tree[a].push(b);
  tree[b].push(a);
}
let Q = [1];
check[1] = 1;
result = 0;
while (Q.length) {
  let u = Q.shift();
  for (let v of tree[u]) {
    if (check[v] === 0) {
      check[v] = check[u] + 1;
      Q.push(v);
    }
  }
}

for (let c of check) {
  if (c === 2 || c === 3) {
    result++;
  }
}
console.log(result);
