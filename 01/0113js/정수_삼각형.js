function solution(triangle) {
  let DP = [];
  for (let tri of triangle) {
    DP.push(Array(tri.length).fill(0));
  }
  DP[0][0] = triangle[0][0];
  for (let y = 1; y < triangle.length; y++) {
    DP[y][0] = DP[y - 1][0] + triangle[y][0];
    for (let x = 1; x < triangle[y].length - 1; x++) {
      DP[y][x] = Math.max(DP[y - 1][x - 1], DP[y - 1][x]) + triangle[y][x];
    }
    DP[y][triangle[y].length - 1] =
      DP[y - 1][triangle[y].length - 2] + triangle[y][triangle[y].length - 1];
  }
  return Math.max(...DP[DP.length - 1]);
}
console.log(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]));
