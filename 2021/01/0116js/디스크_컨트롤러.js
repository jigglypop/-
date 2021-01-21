const solution = (jobs) => {
  let answer = 0;
  let j = 0;
  let time = 0;
  jobs.sort((a, b) => a[0] - b[0]);
  const Q = [];
  while (j < jobs.length || Q.length !== 0) {
    if (jobs.length > j && time >= jobs[j][0]) {
      Q.push(jobs[j++]);
      Q.sort((a, b) => a[1] - b[1]);
      continue;
    }
    if (Q.length !== 0) {
      time += Q[0][1];
      answer += time - Q[0][0];
      Q.shift();
    } else {
      time = jobs[j][0];
    }
  }
  return parseInt(answer / jobs.length);
};
console.log(
  solution([
    [0, 3],
    [1, 9],
    [2, 6],
  ])
);
