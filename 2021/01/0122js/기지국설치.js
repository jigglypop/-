function solution(n, stations, w) {
  let count = 0;
  let idx = 1;
  const range = 2 * w + 1;
  stations.forEach((x, _) => {
    if (x - w > idx) {
      count += Math.ceil((x - w - idx) / range);
    }
    idx = x + w + 1;
  });
  return count + Math.ceil((n - idx + 1) / range);
}
console.log(solution(11, [4, 11], 1));
