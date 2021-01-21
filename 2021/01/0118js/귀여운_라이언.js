// var input = require("fs").readFileSync("./dev/stdin").toString().split("\n");
var input = require("fs").readFileSync("./15565.txt").toString().split("\r\n");

const [N, K] = input[0].split(" ").map(Number);
const nums = input[1].split(" ").map(Number);
let left = 0;
let right = 0;
let count = 0;
let Min = Infinity;
while (true) {
  let R = nums[right] === 1 ? 1 : 0;
  let L = nums[left] === 1 ? 1 : 0;
  if (count + R >= K) {
    Min = Math.min(Min, right - left + 1);
    count -= L;
    left++;
  } else {
    if (right === N) break;
    count += R;
    right++;
  }
}

console.log(Min === Infinity ? -1 : Min);
