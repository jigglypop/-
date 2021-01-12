const gcd = (a, b) => {
  if (a % b === 0) return b;
  return gcd(b, a % b);
};

function solution(w, h) {
  const GCD = gcd(w, h);
  return w * h - (w + h - GCD);
}
console.log(solution(8, 12));
