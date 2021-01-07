function solution(brown, yellow) {
  const all = brown + yellow;
  for (let i = 1; i <= Math.sqrt(all); i++) {
    if (all % i === 0) {
      let [A, B] = [i, all / i].sort((a, b) => b - a);
      if ((A - 2) * 2 + B * 2 === brown) return [A, B];
    }
  }
}
console.log(solution(8, 1));
