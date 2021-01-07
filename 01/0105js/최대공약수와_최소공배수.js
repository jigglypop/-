// function gcd(n, m) {
//   return n % m === 0 ? m : gcd(m, n % m);
// }

// function solution(n, m) {
//   const _gcd = gcd(n, m);
//   return [_gcd, (n * m) / _gcd];
// }
function solution(a, b) {
  var r;
  for (var ab = a * b; (r = a % b); a = b, b = r) {}
  return [b, ab / b];
}
console.log(solution(3, 5));
