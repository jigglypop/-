const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const num = input[0];
let N = num.length;
let plus = Math.ceil(N / 3) * 3 - N;
let front = Array(plus).fill("0").join("");
let nums = front + num;
const table = {
  "000": 0,
  "001": 1,
  "010": 2,
  "011": 3,
  100: 4,
  101: 5,
  110: 6,
  111: 7,
};
let result = [];
for (let i = 0; i < N; i += 3) {
  let temp = [...nums].slice(i, i + 3);
  result.push(table[temp.join("")]);
}
console.log(result.join(""));
