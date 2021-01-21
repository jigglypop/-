// var input = require("fs").readFileSync("./dev/stdin").toString().split("\n");
var input = require("fs").readFileSync("./10025.txt").toString().split("\n");
const [N, K] = input[0].split(" ").map(Number);
const buckets = [];
let Max = 0;
for (let i = 1; i < N + 1; i++) {
  let [g, x] = input[i].split(" ").map(Number);
  buckets.push([g, x]);
  Max = Math.max(Max, x);
}
let front = Array(K).fill(0);
let back = Array(K).fill(0);
let mid = Array(Max).fill(0);
for (let [g, x] of buckets) {
  mid[x] = g;
}
let nums = front.concat(mid).concat(back);
let left = 0;
let right = 2 * K;
let Sum = 0;
for (let i = left; i <= right; i++) {
  Sum += nums[i];
}
let result = Sum;
for (let i = 0; i < nums.length - 2 * K; i++) {
  let temp = [...nums]
    .slice(i, 2 * K + i + 1)
    .reduce((acc, cur) => (acc += cur), 0);
  result = Math.max(result, temp);
}
console.log(result);
