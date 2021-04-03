const rotate90 = (board) => {
  const Y = board.length;
  const X = board[0].length;
  const _board = Array.from(Array(Y), () => Array(X).fill(0));
  for (let x = 0; x < X; x++) {
    for (let y = 0; y < Y; y++) {
      _board[x][y] = board[Y - y - 1][X - x - 1];
    }
  }
  return _board;
};

const rotate180 = (board) => {
  const Y = board.length;
  const X = board[0].length;
  const _board = Array.from(Array(Y), () => Array(X).fill(0));
  for (let x = 0; x < X; x++) {
    for (let y = 0; y < Y; y++) {
      _board[y][x] = board[Y - y - 1][x];
    }
  }
  return _board;
};

const rotate270 = (board) => {
  const Y = board.length;
  const X = board[0].length;
  const _board = Array.from(Array(X), () => Array(Y).fill(0));
  for (let x = 0; x < X; x++) {
    for (let y = 0; y < Y; y++) {
      _board[x][y] = board[y][X - x - 1];
    }
  }
  return _board;
};

function solution(board) {
  return rotate270(board);
}
// console.log(
//   solution([
//     [1, 2, 3],
//     [4, 5, 6],
//     [7, 8, 9],
//   ])
// );
console.log(
  solution([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
  ])
);
