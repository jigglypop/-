function solution(distance, rocks, n) {
  rocks.sort((a, b) => a - b);
  const C = rocks.length - n;
  let start = 0;
  let end = distance;
  let result = 0;
  while (start <= end) {
    let mid = parseInt((start + end) / 2);
    let count = 0;
    let idx = 0;
    let _rocks = [0, ...rocks, distance];
    for (let i = 1; i < _rocks.length - 1; i++) {
      if (_rocks[i] - _rocks[idx] >= mid) {
        count++;
        idx = i;
      }
    }
    if (C <= count) {
      result = mid;
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return result;
}
console.log(solution(25, [2, 14, 11, 21, 17], 2));
