function solution(progresses, speeds) {
  var answer = [];
  while (true) {
    if (!progresses.length) {
      break;
    }
    progresses = progresses.map((x, i) => (x += speeds[i]));
    let temp = 0;
    for (let i = 0; i < progresses.length; i++) {
      if (progresses[i] < 100) break;
      progresses[i] = -1;
      speeds[i] = -1;
      temp++;
    }
    progresses = progresses.filter((x) => x !== -1);
    speeds = speeds.filter((x) => x !== -1);
    if (temp !== 0) {
      answer.push(temp);
    }
  }
  return answer;
}
console.log(solution([93, 30, 55], [1, 30, 5]));
