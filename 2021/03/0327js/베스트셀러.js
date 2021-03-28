// const input = require('fs').readFileSync('/dev/stdin').toString();
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs")
  .readFileSync("./1302.txt")
  .toString()
  .split("\n")
  .map((x) => x.split(" ").map((x) => x.trim()));

const N = parseInt(input[0]);
const table = {};
for (let i = 1; i <= N; i++) {
  const temp = input[i];
  if (!table[temp]) {
    table[temp] = 1;
  } else {
    table[temp]++;
  }
}
let Max = 0;
let result = "";
for (let key of Object.keys(table)) {
  if (table[key] > Max) {
    Max = table[key];
    result = key;
  } else if (table[key] === Max) {
    result = [result, key].sort()[0];
  }
}
console.log(result);
