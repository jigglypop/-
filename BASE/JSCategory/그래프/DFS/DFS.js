const input = require("fs").readFileSync("./2667.txt").toString().split("\r\n");

// const input = require("fs").readFileSync("/dev/stdin", "utf8").toString().split("\r\n");

const N = parseInt(input[0]);
input.shift();
let board = input.map((x) =>
  x
    .toString()
    .split("")
    .map((x) => parseInt(x))
);
class DFS {
  constructor(N) {
    this.N = N;
    this.check = Array(N).fill(Array(N).fill(false));
    this.count = 1;
    this.di = [
      [-1, 0],
      [1, 0],
      [0, 1],
      [0, -1],
    ];
  }
  dfs(sy, sx) {
    let S = [[sy, sx]];
    this.count = 1;
    board[sy][sx] = 0;
    while (S.length) {
      const [y, x] = S.pop();
      for (let [dy, dx] of this.di) {
        const ny = y + dy;
        const nx = x + dx;
        if (0 <= ny && ny < this.N && 0 <= nx && nx < this.N) {
          if (board[ny][nx] === 1) {
            board[ny][nx] = 0;
            this.count++;
            S.push([ny, nx]);
          }
        }
      }
    }
    return this.count;
  }
}

const dfs = new DFS(N);
let count = 0;
let result = [];
for (let y = 0; y < N; y++) {
  for (let x = 0; x < N; x++) {
    if (board[y][x] === 1) {
      count++;
      result.push(dfs.dfs(y, x));
    }
  }
}
console.log(count);
result.sort((a, b) => a - b);
for (let r of result) {
  console.log(r);
}
