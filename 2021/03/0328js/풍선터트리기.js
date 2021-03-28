// const input = require('fs').readFileSync('/dev/stdin').toString();
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs")
  .readFileSync("./2841.txt")
  .toString()
  .split("\n")
  .map((x) => x.split(" ").map((x) => x.trim()));

const [N, P] = input[0].map(Number);
const Lines = Array.from(Array(7), () => Array());
let result = 0;

for (let i = 1; i <= N; i++) {
  const [l, p] = input[i].map(Number);
  const Line = Lines[l];
  while (Line.length) {
    if (Line[Line.length - 1] > p) {
      Line.pop();
      result++;
    } else if (Line[Line.length - 1] === p) {
      Line.pop();
      result--;
      break;
    } else {
      break;
    }
  }
  Line.push(p);
  result++;
}
console.log(result);
