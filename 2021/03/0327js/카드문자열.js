// const input = require('fs').readFileSync('/dev/stdin').toString();
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs")
  .readFileSync("./13417.txt")
  .toString()
  .split("\n")
  .map((x) => x.split(" ").map((x) => x.trim()));

const T = parseInt(input.shift());
for (let i = 0; i < T; i++) {
  const N = parseInt(input.shift());
  const words = input.shift();

  const Q = [[words[0], 0]];
  const result = [];
  while (Q.length) {
    let [_words, i] = Q.shift();
    if (i >= N - 1) {
      result.push(_words);
    } else {
      if (_words > words[i + 1]) {
        Q.push([words[i + 1] + _words, i + 1]);
      } else {
        Q.push([_words + words[i + 1], i + 1]);
      }
    }
  }
  console.log(result.sort()[0]);
}
