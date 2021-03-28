// const input = require('fs').readFileSync('/dev/stdin').toString();
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs")
  .readFileSync("./5568.txt")
  .toString()
  .split("\n")
  .map((x) => x.split(" ").map((x) => x.trim()));

const n = parseInt(input[0]);
const K = parseInt(input[1]);
const nums = [];
for (let i = 2; i < n + 2; i++) {
  nums.push(parseInt(input[i]));
}

const result = new Set();
const perm = (k, used, choice) => {
  if (k > K - 1) {
    result.add([...choice].join(""));
    return;
  }
  for (let i = 0; i < n; i++) {
    if (used & (1 << i)) continue;
    choice.push(nums[i]);
    perm(k + 1, used | (1 << i), choice);
    choice.pop();
  }
};
perm(0, 0, []);
console.log(result.size);
