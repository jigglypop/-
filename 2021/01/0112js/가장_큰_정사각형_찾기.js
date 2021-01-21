function solution(board) {
  let result = 0;
  let resultArr = board.slice();
  //board의 현재값이 1일경우 왼쪽상단 ,위쪽  ,왼쪽 값중에 가장 작은 값..
  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      if (board[i][j] === 1) {
        if (i - 1 < 0 || j - 1 < 0) {
          resultArr[i][j] = board[i][j];
          result = Math.max(resultArr[i][j], result);
          continue;
        }
        resultArr[i][j] =
          Math.min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) +
          board[i][j];
        result = Math.max(resultArr[i][j], result);
      }
    }
  }
  return result ** 2;
}
console.log(
  solution([
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 1, 0],
  ])
);
