// const input = require('fs').readFileSync('/dev/stdin').toString().split("\n");
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));
let input = require("fs").readFileSync("./1343.txt").toString().split("\n");

let words = input[0]
  .split(/([.]+)|([X]+)/g)
  .filter((x) => x !== undefined && x !== "");

let result = "";
let _word = [];
for (let word of words) {
  let temp = word;
  if (word[0] === "X") {
    if (word.length % 2 === 1) {
      result = "-1";
      break;
    } else {
      let four = parseInt(word.length / 4);
      let two = parseInt((word.length % 4) / 2);
      temp = "AAAA".repeat(four) + "BB".repeat(two);
      word = temp;
    }
  }
  _word.push(temp);
}
console.log(result === "-1" ? "-1" : _word.join(""));
