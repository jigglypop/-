function solution(s) {
  const lists = s.split(" ");
  return [Math.min(...lists), Math.max(...lists)];
}
console.log(solution("1 2 3 4"));
