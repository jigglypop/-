function solution(n, base) {
  var answer = [];
  console.log(parseInt(n / base));
  while (true) {
    if (parseInt(n / base) === 0) {
      answer.push(n);
      break;
    }
    answer.push(n % base);
    n = parseInt(n / base);
  }
  return answer.reverse().join("");
}
console.log(solution(15, 3));
