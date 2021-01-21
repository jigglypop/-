// const input = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n");
const input = require("fs")
  .readFileSync("./2217.txt")
  .toString()
  .trim()
  .split("\n");

let N = parseInt(input[0]);
let nums = [];
for (let i = 1; i < N + 1; i++) {
  nums.push(parseInt(input[i]));
}
nums.sort((a, b) => a - b);
let Max = nums[0] * N;
for (let num of nums) {
  Max = Math.max(Max, num * N);
  N--;
}
console.log(Max);
