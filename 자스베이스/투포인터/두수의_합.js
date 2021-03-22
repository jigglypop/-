// var input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n")
var input = require("fs")
  .readFileSync("./3273.txt")
  .toString()
  .trim()
  .split("\r\n");

const n = parseInt(input[0]);
let nums = input[1].split(" ").map(Number);
const x = parseInt(input[2]);
nums = nums.sort((a, b) => a - b);
let left = 0,
  right = n - 1,
  result = 0;
while (left < right) {
  if (nums[left] + nums[right] >= x) {
    if (nums[left] + nums[right] === x) result++;
    right--;
  } else if (nums[left] + nums[right] < x) {
    if (right === n) break;
    left++;
  }
}
console.log(result);
