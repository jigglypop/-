function solution(lines) {
  var answer = 0;
  console.log(lines);
  for (let line of lines) {
    time = line.replace("2016-09-15 ", "").split(" ");
    console.log(time);
  }
  console.log(3000 / 0.001);
  return answer;
}
console.log(
  solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
);
