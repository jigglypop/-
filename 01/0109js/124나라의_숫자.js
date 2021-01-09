function solution(n) {
  var answer = [];
  while (true) {
    if (parseInt(n / 3) === 0) {
      answer.push(n);
      break;
    } else if (n % 3 === 0) {
      answer.push(4);
      n = parseInt(n / 3) - 1;
    } else {
      answer.push(n % 3);
      n = parseInt(n / 3);
    }
  }
  return answer.reverse().join("").replace(/0/g, "");
}
console.log(solution(6));
