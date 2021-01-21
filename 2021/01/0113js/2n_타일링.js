function solution(n) {
  var answer = 0;
  var DP = Array(n).fill(0);
  DP[0] = 1;
  DP[1] = 2;
  for (var i = 2; i < n; i++) {
    var a = DP[i - 1] + DP[i - 2];
    DP[i] = a % 1000000007;
  }
  return DP[n - 1];
}
console.log(solution(4));
