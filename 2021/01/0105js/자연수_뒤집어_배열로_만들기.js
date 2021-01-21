function solution(num) {
  return num
    .toString()
    .split("")
    .reverse()
    .map((a) => parseInt(a));
}
console.log(solution(12345));
