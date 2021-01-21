// const input = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n");
const input = require("fs")
  .readFileSync("./10422.txt")
  .toString()
  .trim()
  .split("\n");

const N = parseInt(input[0]);
var mod = 1000000007;
let Max = 0;
let nums = [];
for (let i = 1; i < N + 1; i++) {
  let a = parseInt(input[i]);
  Max = Math.max(Max, a);
  nums.push(a);
}
var DP = Array(5001).fill(0);
DP[0] = 1;
DP[2] = 1;
for (let i = 3; i <= 5000; i++) {
  for (let j = 2; j <= i; j++) {
    if (j - 2 >= 0 && i - j >= 0) {
      DP[i] += DP[j - 2] * DP[i - j];
      DP[i] = DP[i] % mod;
    }
  }
}

for (let num of nums) {
  if (num % 2 === 1) {
    console.log(0);
  } else {
    console.log(DP[num]);
  }
}
