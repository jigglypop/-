function solution(n) {
  const check = Array(n + 1)
    .fill(0)
    .map((_, i) => i);
  for (let i = 1; i <= n; i++) {
    check[i] += check[i - 1];
  }
  let count = (left = right = 0);
  while (true) {
    const Sum = check[right] - check[left];
    if (Sum >= n) {
      if (Sum === n) count++;
      left++;
    } else if (Sum < n) {
      if (right === n) break;
      right++;
    }
  }
  return count;
}
console.log(solution(15));
