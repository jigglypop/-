// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs")
  .readFileSync("./9375.txt")
  .toString()
  .trim()
  .split("\n");

const T = +input.shift();

let output = "";
for (let t = 0; t < T; t++) {
  const n = input.shift();
  const dict = {};
  for (let i = 0; i < n; i++) {
    const [, type] = input.shift();
    if (!dict[type]) dict[type] = 0;
    dict[type]++;
  }

  let result = 1;
  for (value of Object.values(dict)) {
    result *= value + 1;
  }
  output += result - 1 + "\n";
}
console.log(output);
