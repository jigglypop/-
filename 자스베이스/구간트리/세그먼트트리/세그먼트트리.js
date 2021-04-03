// const input = require('fs').readFileSync('/dev/stdin').toString().split("\n");
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs").readFileSync("./10868.txt").toString().split("\n");
const [N, M] = input.shift().split(" ").map(Number);
const board = input.splice(0, N).map((x) => parseInt(x));
const log2 = 1 << (Math.ceil(Math.log2(N)) + 1);
const tree = Array(log2).fill(0);
const INF = Number.MAX_SAFE_INTEGER;

const init = (x, s, e) => {
  if (s === e) {
    tree[x] = board[e];
    return tree[x];
  }
  mid = parseInt((s + e) / 2);
  tree[x] = Math.min(init(2 * x, s, mid), init(2 * x + 1, mid + 1, e));
  return tree[x];
};

init(1, 0, N - 1);
const query = (x, s, e, S, E) => {
  if (S > e || s > E) return INF;
  if (s >= S && e <= E) return tree[x];
  mid = parseInt((s + e) / 2);
  return Math.min(
    query(2 * x, s, mid, S, E),
    query(2 * x + 1, mid + 1, e, S, E)
  );
};

for (let temp of input) {
  const [start, end] = temp.split(" ").map((x) => parseInt(x));
  console.log(query(1, 0, N - 1, start - 1, end - 1));
}
