function solution(n, coins) {
  let DP = Array(n + 1).fill(0);
  DP[0] = 1;
  for (let coin of coins) {
    for (let i = coin; i <= n; i++) {
      DP[i] += DP[i - coin];
    }
  }
  return DP[n];
}
console.log(solution(5, [1, 2, 5]));
