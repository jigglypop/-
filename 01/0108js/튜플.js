function solution(s) {
  var answer = [];
  let tuples = JSON.parse(s.replace(/{/g, "[").replace(/}/g, "]")).sort(
    (a, b) => a.length - b.length
  );
  let deleted = new Set();
  for (let tuple of tuples) {
    for (let i = 0; i < tuple.length; i++) {
      if (!deleted.has(tuple[i])) {
        deleted.add(tuple[i]);
        answer.push(parseInt(tuple[i]));
        break;
      }
    }
  }
  return answer;
}
console.log(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"));
