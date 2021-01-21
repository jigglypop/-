function solution(numbers, target) {
  let answer = 0;
  const n = numbers.length;
  const N = 1 << n;
  for (let i = 0; i < N; i++) {
    let temp = 0;
    for (let j = 0; j < n; j++) {
      if (i & (1 << j)) {
        temp -= numbers[j];
      } else {
        temp += numbers[j];
      }
    }
    if (target === temp) answer++;
  }
  return answer;
}
console.log(solution([1, 1, 1, 1, 1], 3));
