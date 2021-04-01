// const input = require('fs').readFileSync('/dev/stdin').toString().split("\n");
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs").readFileSync("./11478.txt").toString().split("\n");
const words = [...input[0]];
const word_set = new Set();
for (let i = 1; i <= words.length; i++) {
  for (let j = 0; j <= words.length - i; j++) {
    word_set.add(words.slice(j, j + i).join(""));
  }
}
console.log(word_set.size);
