function solution(n) {
  if (n === 1) return [1];
  if (n === 2) return [1, 2, 3];
  let board = Array.from(Array(n), (_, i) => Array(i + 1).fill(0));
  let count = 0;
  const di = [
    [1, 0],
    [0, 1],
    [-1, -1],
  ];
  let Q = [[0, 0, 0]];
  while (Q.length) {
    let [q, y, x] = Q.shift();
    count += 1;
    board[y][x] = count;
    let ny = y + di[q][0];
    let nx = x + di[q][1];
    if (0 <= ny && ny < n && 0 <= nx && nx <= ny) {
      if (board[ny][nx] === 0) {
        Q.push([q, ny, nx]);
      } else {
        q = (q + 1) % 3;
        ny = y + di[q][0];
        nx = x + di[q][1];
        if (board[ny][nx] === 0) {
          Q.push([q, ny, nx]);
        }
      }
    } else {
      q = (q + 1) % 3;
      ny = y + di[q][0];
      nx = x + di[q][1];
      Q.push([q, ny, nx]);
    }
  }
  return board.flat();
}

// function solution(n) {
//   let a = Array(n).fill().map((_, i) => Array(i + 1).fill())
//   let row = -1
//   let col = 0
//   let fill = 0
//   for (let i = n; i > 0; i -= 3) {
//     a[++row][col] = ++fill
//     for (let j = 0; j < i - 1; j++) a[++row][col] = ++fill
//     for (let j = 0; j < i - 1; j++) a[row][++col] = ++fill
//     for (let j = 0; j < i - 2; j++) a[--row][--col] = ++fill
//   }
//   return a.flat()
// }
console.log(solution(3));
