function solution(n) {
  return n
    .toString()
    .split("")
    .reduce((result, a, _) => (result += parseInt(a)), 0);
}
console.log(solution(123));
