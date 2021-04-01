// const input = require('fs').readFileSync('/dev/stdin').toString();
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs").readFileSync("./11497.txt").toString().split("\n");
const T = input.shift();
for (let i = 0; i < T; i++) {
  const N = input.shift();
  const nums = input.shift().split(" ").map(Number);
  nums.sort();
  const A = [];
  const B = [];
  for (let i = 0; i < nums.length; i += 2) {
    A.push(nums[i]);
    if (nums[i + 1] !== undefined) {
      B.push(nums[i + 1]);
    }
  }
  const _nums = [...A, ...B.reverse()];
  let Max = Math.abs(_nums[0] - _nums[_nums.length - 1]);
  for (let i = 0; i < _nums.length - 1; i++) {
    Max = Math.max(Math.abs(_nums[i] - _nums[i + 1]), Max);
  }
  console.log(Max);
}
