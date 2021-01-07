function solution(s) {
  var lists = [];
  for (let i = 0; i < s.length; i++) {
    lists.push(s.charAt(i));
  }
  return lists.sort().reverse().join("");
}
console.log(solution("Zbcdefg"));
