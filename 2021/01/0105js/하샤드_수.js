function solution(n) {
  return (
    n %
      n
        .toString()
        .split("")
        .reduce((result, a) => (result += parseInt(a)), 0) ===
    0
  );
}
console.log(solution(18));
