// const input = require('fs').readFileSync('/dev/stdin').toString();
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs")
  .readFileSync("./1269.txt")
  .toString()
  .split("\n")
  .map((x) => x.split(" ").map((x) => x.trim()));

const A = input[1].map(Number);
const B = input[2].map(Number);
const table = {};
for (let a of A) {
  table[a] = true;
}
for (let b of B) {
  if (table[b]) {
    delete table[b];
  } else {
    table[b] = true;
  }
}
console.log(Object.keys(table).length);
