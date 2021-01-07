function solution(n) {
  return Math.floor(Math.sqrt(n)) === Math.sqrt(n)
    ? (Math.sqrt(n) + 1) ** 2
    : -1;
}

console.log(solution(121));
