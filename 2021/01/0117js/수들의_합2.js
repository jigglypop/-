// var input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n")
var input = require("fs")
  .readFileSync("./2003.txt")
  .toString()
  .trim()
  .split("\r\n");

const [N, M] = input[0].split(" ").map(Number);
let nums = input[1].split(" ").map(Number);
let sum = 0,
  left = 0,
  right = 0,
  result = 0;
while (true) {
  if (sum >= M) {
    if (sum === M) result++;
    sum -= nums[left];
    left++;
  } else if (sum < M) {
    if (right === N) break;
    sum += nums[right];
    right++;
  }
}
console.log(result);
