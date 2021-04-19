// const input = require('fs').readFileSync('/dev/stdin').toString();
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));
let input = require("fs")
  .readFileSync("./13565.txt")
  .toString()
  .split("\n")
  .map((x) => x.split(" ").map((x) => x.trim()));
const [Y, X] = input.shift().map(Number);
let board = input.map((x) => x[0].split(""));

const dfs = (sy, sx) => {
  const visited = Array.from(Array(Y), () => Array(X).fill(false));
  const di = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
  ];
  const Q = [[sy, sx]];
  board[sy][sx] = "2";
  visited[sy][sx] = true;
  while (Q.length) {
    let [y, x] = Q.shift();
    for (let [dy, dx] of di) {
      let [ny, nx] = [y + dy, x + dx];
      if (0 <= ny && ny < Y && 0 <= nx && nx < X) {
        if (board[ny][nx] === "0" && !visited[ny][nx]) {
          Q.push([ny, nx]);
          visited[ny][nx] = true;
          board[ny][nx] = "2";
        }
      }
    }
  }
};

for (let x = 0; x < X; x++) {
  if (board[0][x] === "0") {
    dfs(0, x);
  }
}
let result = "NO";
for (let x = 0; x < X; x++) {
  if (board[Y - 1][x] === "2") {
    result = "YES";
    break;
  }
}
console.log(result);
