// const input = require('fs').readFileSync('/dev/stdin').toString();
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs")
  .readFileSync("./7785.txt")
  .toString()
  .split("\n")
  .map((x) => x.split(" ").map((x) => x.trim()));

const T = input[0];
const temp = {};

for (let i = 1; i <= T; i++) {
  const [name, value] = input[i];
  if (value === "enter") {
    temp[name] = true;
  } else {
    delete temp[name];
  }
}
console.log(
  Object.keys(temp)
    .sort((a, b) => (a < b ? 1 : a > b ? -1 : 0))
    .join("\n")
);
