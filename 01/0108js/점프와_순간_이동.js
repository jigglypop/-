function solution(n) {
  var answer = 0;
  while (n > 0) {
    if (n % 2 !== 0) {
      n = n - 1;
      answer = answer + 1;
    } else {
      n = n / 2;
    }
  }
  return answer;
}
console.log(solution(5000));
// 1000000000
