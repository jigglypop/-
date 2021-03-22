// const input = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n");
const input = require("fs")
  .readFileSync("./10994.txt")
  .toString()
  .trim()
  .split("\n");

let N = parseInt(input[0]);
var board = Array.from(Array(4 * N - 3), () => Array(4 * N - 3).fill(" "));

let L = 2 * N - 1;

const print = (board) => {
  for (let b of board) {
    console.log(b.join(""));
  }
};

const draw = (d, L) => {
  for (let x = 0; x < L; x++) {
    board[d][d + x] = "*";
    board[d + L - 1][d + x] = "*";
    board[d + x][d] = "*";
    board[d + x][d + L - 1] = "*";
  }
};
let start = 2 * N - 2;
for (let i = 1; i <= N; i++) {
  draw(start, 4 * i - 3);
  start -= 2;
}
print(board);
