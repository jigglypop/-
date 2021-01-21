function getSec(time) {
  time = time.split(":");
  return time[0] * 3600000 + time[1] * 60000 + time[2] * 1000;
}

function solution(lines) {
  lines = lines.map((e) => e.split(" "));
  let finishTime = lines.map((e) => getSec(e[1]));
  let startTime = lines.map(
    (e, i) => finishTime[i] - e[2].replace("s", "") * 1000 + 1
  );
  let points = startTime.concat(finishTime).sort((a, b) => a - b);
  let answer = 0;
  for (let i = 0; i < points.length; i++) {
    let cnt = 0;
    for (let j = 0; j < startTime.length; j++) {
      if (points[i] <= finishTime[j] && points[i] + 999 >= startTime[j]) cnt++;
    }
    if (answer < cnt) answer = cnt;
  }
  return answer;
}
console.log(
  solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s",
  ])
);
