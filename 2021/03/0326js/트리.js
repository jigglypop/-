// const input = require('fs').readFileSync('/dev/stdin').toString();
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs")
  .readFileSync("./1068.txt")
  .toString()
  .split("\n")
  .map((x) => x.split(" ").map((x) => x.trim()));

const N = parseInt(input[0]);
const parents = input[1].map(Number);
const M = parseInt(input[2]);
const tree = Array.from(Array(N), () => Array());

for (let i = 0; i < N; i++) {
  if (parents[i] !== -1) {
    tree[parents[i]].push(i);
  }
}
let isdeleted = Array(N).fill(false);

const remover = (u) => {
  isdeleted[u] = true;
  for (let v of tree[u]) {
    remover(v);
  }
};
remover(M);
let result = 0;
const dfs = (u) => {
  let count = 0;
  for (let v of tree[u]) {
    if (!isdeleted[v]) {
      dfs(v);
      count++;
    }
  }
  if (count === 0) {
    result++;
  }
};
if (!isdeleted[0]) dfs(0);
console.log(result);
