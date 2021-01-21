function solution(n, s) {
  if (n > s) return [-1];
  let rest = s % n;
  var answer = Array(n).fill(Math.floor(s / n));
  for (let i = answer.length - 1; i >= 0; i--) {
    if (rest === 0) break;
    answer[i]++;
    rest--;
  }
  return answer;
}
console.log(solution(2, 9));
