// const fs = require('fs');
// const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const input = require("fs")
  .readFileSync("./5397.txt")
  .toString()
  .trim()
  .split("\n");

const N = input[0];
for (let i = 1; i <= N; i++) {
  let words = input[i];
  const left = [];
  const right = [];
  for (let word of words) {
    if (word === "<") {
      if (left.length) right.push(left.pop());
    } else if (word === ">") {
      if (right.length) left.push(right.pop());
    } else if (word === "-") {
      if (left.length) left.pop();
    } else {
      left.push(word);
    }
  }
  console.log(left.join("") + right.reverse().join(""));
}
