function solution(Y, X, board) {
  const block = Array.from(Array(X), () => Array(Y).fill(0));
  board = board.map((x) => x.split(""));
  console.log(board);
  for (let y = 0; y < Y; y++) {
    for (let x = 0; x < X; x++) {
      block[y][x] = board[x][y];
    }
  }
  console.log(block);
  var answer = 0;
  return answer;
}
console.log(
  solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
);
