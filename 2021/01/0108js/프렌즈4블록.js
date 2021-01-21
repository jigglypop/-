function solution(Y, X, board) {
  var pointSet;
  var block = Array.from(Array(X), () => Array(Y).fill(0));
  board = board.map((x) => x.split(""));
  for (let y = 0; y < Y; y++) {
    for (let x = 0; x < X; x++) {
      block[x][y] = board[y][x];
    }
  }
  block = block.map((x) => x.reverse());

  let answer = 0;
  while (true) {
    pointSet = new Set();
    for (let y = 0; y < X - 1; y++) {
      for (let x = 0; x < Y - 1; x++) {
        if (
          block[y][x] === block[y + 1][x] &&
          block[y + 1][x] === block[y][x + 1] &&
          block[y][x + 1] === block[y + 1][x + 1] &&
          block[y + 1][x + 1] === block[y][x] &&
          block[y][x] !== "*" &&
          block[y + 1][x] !== "*" &&
          block[y][x + 1] !== "*" &&
          block[y + 1][x + 1] !== "*"
        ) {
          pointSet.add(`${y}__${x}`);
          pointSet.add(`${y + 1}__${x}`);
          pointSet.add(`${y}__${x + 1}`);
          pointSet.add(`${y + 1}__${x + 1}`);
        }
      }
    }
    let _point = [...pointSet];
    if (_point.length === 0) break;
    answer += _point.length;

    for (let p of pointSet) {
      const [y, x] = p.split("__").map(Number);
      block[y][x] = "*";
    }
    block = block
      .map((X) => X.filter((x) => x !== "*"))
      .map((x) =>
        Y - x.length !== 0 ? x.concat(Array(Y - x.length).fill("*")) : x
      );
  }
  return answer;
}
console.log(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]));
