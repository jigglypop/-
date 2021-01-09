function solution(priorities, location) {
  let answer = 0;
  priorities = priorities.map((x, i) => [x, i]);
  while (priorities.length) {
    let Max = priorities.reduce((acc, cur) => (acc = Math.max(acc, cur[0])), 0);
    let [q, i] = priorities.shift();
    if (q !== Max) {
      priorities.push([q, i]);
    } else {
      answer++;
      if (i === location) {
        break;
      }
    }
  }
  return answer;
}
console.log(solution([2, 1, 3, 2], 2));
