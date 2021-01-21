const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
// const input = require("fs")
//   .readFileSync("./1051.txt")
//   .toString()
//   .trim()
//   .split("\r\n");

const [Y, X] = input[0].split(" ").map(Number);
let board = input.slice(1, input.length).map((x) => x.split("").map(Number));
let R = Math.min(Y, X);
const isValid = (R) => {
  let r = R - 1;
  for (let y = 0; y < Y - r; y++) {
    for (let x = 0; x < X - r; x++) {
      if (
        board[y][x] === board[y + r][x] &&
        board[y + r][x] === board[y][x + r] &&
        board[y][x + r] === board[y + r][x + r] &&
        board[y + r][x + r] === board[y][x]
      ) {
        return true;
      }
    }
  }

  return false;
};
let Result = 1;
while (R > 1) {
  if (isValid(R)) {
    Result = R * R;
    break;
  }
  R--;
}
console.log(Result);
