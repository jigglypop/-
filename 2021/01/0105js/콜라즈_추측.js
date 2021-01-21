function solution(num, count = 0) {
  return num == 1
    ? count >= 500
      ? -1
      : count
    : solution(num % 2 == 0 ? num / 2 : num * 3 + 1, ++count);
}
console.log(solution(626331));
