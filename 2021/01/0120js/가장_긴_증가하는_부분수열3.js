const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
// const input = require("fs")
//   .readFileSync("./12738.txt")
//   .toString()
//   .trim()
//   .split("\n");

const N = parseInt(input[0]);
const nums = input[1].split(" ").map(Number);

const lower_bound = (M, S) => {
  let start = 0;
  let end = nums.length - 1;
  let result = 0;
  while (start <= end) {
    let mid = parseInt((start + end) / 2);
    if (S[mid] < M) {
      result = mid;
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return result;
};
let S = [nums[0]];
for (let num of nums) {
  if (S[S.length - 1] < num) {
    S.push(num);
  } else {
    let idx = lower_bound(num, S);
    S[idx] = num;
  }
}
console.log(S.length);
