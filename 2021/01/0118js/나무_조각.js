// var input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n")
var input = require("fs")
  .readFileSync("./2947.txt")
  .toString()
  .trim()
  .split("\r\n");

let nums = input[0].split(" ").map(Number);
while (true) {
  let temp = true;
  for (let i = 0; i < 4; i++) {
    if (nums[i] > nums[i + 1]) {
      [nums[i + 1], nums[i]] = [nums[i], nums[i + 1]];
      console.log(nums.join(" "));
      temp = false;
    }
  }
  if (temp) break;
}
