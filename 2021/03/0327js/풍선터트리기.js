// const input = require('fs').readFileSync('/dev/stdin').toString();
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs").readFileSync("./2346.txt").toString().split("\n");

let N = Number(input[0]);
let Q = input[1].split(" ").map((v, i) => [i + 1, Number(v)]);

let _N = N;
let idx = 0;
let str = "";

for (let i = 0; i < _N; i++) {
  str += Q[idx][0] + " ";
  let move = Q[idx][1];
  if (move > 0) move--;
  Q.splice(idx, 1);
  idx += move;
  N--;
  if (!N) continue;
  if (idx > 0) {
    idx = idx % N;
  } else {
    idx = (idx + N) % N;
    if (idx < 0) idx = N + idx;
  }
}

console.log(str.trim());
