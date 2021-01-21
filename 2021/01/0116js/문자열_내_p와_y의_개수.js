function solution(s) {
  let P = 0;
  let Y = 0;
  for (let S of s) {
    if (S === "Y" || S === "y") Y++;
    if (S === "P" || S === "p") P++;
  }
  return P === Y;
}
console.log(solution("Pyy"));
