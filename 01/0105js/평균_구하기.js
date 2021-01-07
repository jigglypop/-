function solution(n) {
  return n.reduce((result, x) => (result += x)) / n.length;
}

console.log(solution(3, 12));
