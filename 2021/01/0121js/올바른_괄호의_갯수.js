function solution(n) {
  const DP = Array(n + 1).fill(0);
  DP[0] = 1;
  for (let i = 1; i <= n; i++) {
    for (let j = 0; j < i; j++) {
      DP[i] += DP[i - j - 1] * DP[j];
    }
  }
  return DP[n];
}
console.log(solution(5));
