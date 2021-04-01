// const input = require('fs').readFileSync('/dev/stdin').toString().split("\n");
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs")
  .readFileSync("./2847.txt")
  .toString()
  .split("\n")
  .map((x) => x.split(" ").map((x) => x.trim()));

input.shift();
const nums = input.reverse();
let result = 0;
for (let i = 0; i < nums.length - 1; i++) {
  if (nums[i] - nums[i + 1] <= 0) {
    let gap = nums[i + 1] - nums[i] + 1;
    nums[i + 1] -= gap;
    result += gap;
  }
}
console.log(result);
