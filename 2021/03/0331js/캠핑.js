// const input = require('fs').readFileSync('/dev/stdin').toString();
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs")
  .readFileSync("./4796.txt")
  .toString()
  .split("\n")
  .map((x) => x.split(" ").map((x) => x.trim()));

for (let i = 0; i < input.length - 1; i++) {
  const [L, P, V] = input[i];
  console.log(`Case ${i + 1}: ${parseInt(V / P) * L + (V % P)}`);
}
