function solution(n) {
  if (n % 2 === 1) return 0;
  const MOD = 1000000007;
  const DP = Array(5010).fill(0);
  DP[0] = 1;
  DP[2] = 3;
  for (let i = 4; i <= n; i = i + 2) {
    DP[i] = DP[i - 2] * 3;
    for (let j = i - 4; j >= 0; j = j - 2) {
      DP[i] = DP[i] + DP[j] * 2;
    }
    DP[i] = DP[i] % MOD;
  }
  return DP[n];
}
console.log(solution(6));
