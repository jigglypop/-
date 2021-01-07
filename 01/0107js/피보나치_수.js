function solution(num) {
  let memo = [0, 1];
  for (var i = 2; i < num + 1; i++) {
    memo[i] = (memo[i - 1] + memo[i - 2]) % 1234567;
  }
  return memo[num];
}
console.log(solution(3));
