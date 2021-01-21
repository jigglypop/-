function solution(n, times) {
  times.sort((a, b) => a - b);
  let start = 1;
  let end = n * times[times.length - 1];
  let result = end;
  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    let count = 0;
    times.forEach((time) => {
      count += Math.floor(mid / time);
      if (count >= n) {
        result = Math.min(mid, result);
        return;
      }
    });
    if (count < n) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return result;
}
console.log(solution(6, [7, 10]));
