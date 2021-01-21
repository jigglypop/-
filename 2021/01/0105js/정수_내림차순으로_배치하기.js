function solution(num) {
  return parseInt(
    num
      .toString()
      .split("")
      .map((a) => parseInt(a))
      .sort((a, b) => b - a)
      .join("")
  );
}
console.log(solution(118372));
