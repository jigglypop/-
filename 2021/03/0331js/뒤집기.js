// const input = require('fs').readFileSync('/dev/stdin').toString().split("\n");
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs").readFileSync("./1439.txt").toString().split("\n");
const words = input[0];
let count = { 0: 0, 1: 0 };
let now = "";
for (let word of words) {
  if (word !== now) {
    now = word;
    count[word] += 1;
  }
}
console.log(Math.min(count[0], count[1]));
