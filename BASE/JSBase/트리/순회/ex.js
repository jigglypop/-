class Node {
  constructor(value = null) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

var fs = require("fs");
// const input = fs.readFileSync('dev/stdin').toString().split('\n');
var input = fs.readFileSync("./ex.txt").toString().split("\r\n");

const N = parseInt(input[0]);
console.log(N);
