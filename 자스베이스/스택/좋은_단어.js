// var input = require("fs").readFileSync("./dev/stdin").toString().split("\n");
var input = require("fs").readFileSync("./3986.txt").toString().split("\r\n");

const N = parseInt(input[0]);
let result = 0;
for (let j = 1; j < N + 1; j++) {
  let S = [];
  let words = input[j];
  for (let i = 0; i < words.length; i++) {
    if (!S.length) {
      S.push(words[i]);
    } else {
      if (S[S.length - 1] === words[i]) {
        S.pop();
      } else {
        S.push(words[i]);
      }
    }
  }
  if (!S.length) result++;
}
console.log(result);
