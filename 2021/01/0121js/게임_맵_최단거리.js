function solution(maps) {
  let Y = maps.length;
  let X = maps[0].length;
  let visited = Array.from(Array(Y), () => Array(X).fill(-1));
  visited[0][0] = 1;
  let Q = [[0, 0]];
  let di = [
    [-1, 0],
    [1, 0],
    [0, 1],
    [0, -1],
  ];
  while (Q.length) {
    let [y, x] = Q.shift();
    for (let [dy, dx] of di) {
      let [ny, nx] = [y + dy, x + dx];
      if (0 <= ny && ny < Y && 0 <= nx && nx < X) {
        if (visited[ny][nx] === -1 && maps[ny][nx] === 1) {
          visited[ny][nx] = visited[y][x] + 1;
          Q.push([ny, nx]);
        }
      }
    }
  }
  return visited[Y - 1][X - 1];
}
console.log(
  solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
  ])
);
