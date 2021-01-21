function solution(board) {
  var N = board.length;
  let DP = Array.from(Array(N), () =>
    Array.from(Array(N), () => Array(4).fill(-1))
  );
  const go = (y, x, d) => {
    let di = [
      [-1, 0],
      [1, 0],
      [0, 1],
      [0, -1],
    ];
    if (DP[y][x][d] !== -1) {
      return DP[y][x][d];
    }
    if (x === 0 && y === 0) {
      return 0;
    }
    DP[y][x][d] = Infinity;
    for (let _d = 0; _d < 4; _d++) {
      let [ny, nx] = [y + di[_d][0], x + di[_d][1]];
      if (0 <= ny && ny < N && 0 <= nx && nx < N) {
        if (board[ny][nx] !== 1) {
          let temp = 500;
          if (_d === d) temp = 100;
          DP[y][x][d] = Math.min(DP[y][x][d], go(ny, nx, _d) + temp);
        }
      }
    }
    return DP[y][x][d];
  };
  for (let i = 0; i < 4; i++) {
    go(N - 1, N - 1, i);
  }
  console.log(DP);
  return Math.min(
    DP[N - 1][N - 1][0],
    DP[N - 1][N - 1][1],
    DP[N - 1][N - 1][2],
    DP[N - 1][N - 1][3]
  );
}
console.log(
  solution([
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
  ])
);
