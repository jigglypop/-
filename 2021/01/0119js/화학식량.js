// const input = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n");
const input = require("fs")
  .readFileSync("./2257.txt")
  .toString()
  .trim()
  .split("\n");

const words = input[0];
const atom = { H: 1, C: 12, O: 16 };
let S = [];
for (let word of words) {
  if (word === "(") {
    S.push(word);
  } else if (atom[word]) {
    S.push(atom[word]);
  } else if (word === ")") {
    let temp = 0;
    while (true) {
      let num = S.pop();
      if (num === "(") break;
      temp += num;
    }
    S.push(temp);
  } else {
    S.push(S.pop() * parseInt(word));
  }
}
console.log(S.reduce((acc, cur) => (acc += cur), 0));
