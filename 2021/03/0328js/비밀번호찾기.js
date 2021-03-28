// const input = require('fs').readFileSync('/dev/stdin').toString();
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs")
  .readFileSync("./17219.txt")
  .toString()
  .split("\n")
  .map((x) => x.split(" ").map((x) => x.trim()));

const [N, M] = input[0].map(Number);
const passwords = {};
for (let i = 1; i <= N; i++) {
  const [a, b] = input[i];
  passwords[a] = b;
}
for (let i = 1 + N; i <= N + M; i++) {
  const site = input[i];
  console.log(passwords[site]);
}
