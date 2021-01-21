// const input = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n");
const input = require("fs")
  .readFileSync("./11058.txt")
  .toString()
  .trim()
  .split("\n");

const N = parseInt(input[0]);
const DP = Array.from(Array(102), (_, i) => i);
for (let i = 6; i < 101; i++) {
  DP[i] = Math.max(DP[i - 3] * 2, DP[i - 4] * 3, DP[i - 5] * 4);
}
console.log(DP[N]);
