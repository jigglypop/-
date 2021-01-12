function solution(s) {
  var answer = 1;
  let S = [];
  for (let i = 0; i < s.length; i++) {
    if (S.length === 0 || S[S.length - 1] !== s[i]) {
      S.push(s[i]);
    } else {
      S.pop();
    }
  }
  if (S.length) {
    answer = 0;
  }
  return answer;
}
console.log(solution("b"));
