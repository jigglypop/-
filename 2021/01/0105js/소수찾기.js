function solution(n) {
  var answer = 0;
  var primes = Array(n + 1).fill(false);
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (primes[i] === false) {
      for (let j = i + i; j <= n; j += i) {
        primes[j] = true;
      }
    }
  }
  for (let i = 2; i <= n; i++) {
    if (primes[i] === false) {
      answer += 1;
    }
  }
  return answer;
}
console.log(solution(10));
