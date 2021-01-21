const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
// const input = require("fs").readFileSync("./4889.txt").toString().trim().split("\n");

for (let i = 1; i < input.length; i++) {
  let words = input[i - 1].split("");
  let j = 0;
  let S = [];
  for (let i = 0; i < words.length; i++) {
    let word = words[i];
    if (word === "{") {
      S.push("{");
    } else {
      if (S.length) {
        S.pop();
      } else {
        j++;
        S.push("{");
      }
    }
  }
  if (S.length) {
    j += S.length / 2;
  }
  console.log(`${i}. ${j}`);
}
