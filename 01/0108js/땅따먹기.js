function solution(land) {
  let DP = [land[0]].concat(
    Array.from(Array(land.length - 1), () => Array(4).fill(0))
  );
  for (let y = 1; y < land.length; y++) {
    for (let x = 0; x < 4; x++)
      DP[y][x] =
        DP[y - 1]
          .filter((_, i) => i !== x)
          .reduce((acc, cur) => (acc > cur ? acc : cur)) + land[y][x];
  }
  return DP[land.length - 1].reduce((acc, cur) => (acc > cur ? acc : cur));
}
console.log(
  solution([
    [1, 2, 3, 5],
    [5, 6, 7, 8],
    [4, 3, 2, 1],
  ])
);
