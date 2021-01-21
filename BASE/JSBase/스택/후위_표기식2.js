// var input = require("fs").readFileSync("./dev/stdin").toString().split("\n");
// var input = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n")
var input = require("fs")
  .readFileSync("./1935.txt")
  .toString()
  .trim()
  .split("\r\n");

const N = parseInt(input[0]);
let words = input[1];
let nums = [];
for (let i = 2; i < N + 2; i++) {
  nums.push(input[i]);
}
let S = [];
words.split("").forEach((e) => {
  if (e.match(/[+|\-|*|/]/g)) {
    let a = S.pop();
    let b = S.pop();
    S.push(eval(b + e + a));
  } else {
    S.push(parseInt(nums[e.charCodeAt() - 65]));
  }
});
console.log(S[0].toFixed(2));
