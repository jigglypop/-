function solution(array, commands) {
  var answer = [];
  for (let command of commands) {
    let [start, end, k] = command;
    let temp = array.slice(start - 1, end).sort((a, b) => a - b);
    answer.push(temp[k - 1]);
  }
  return answer;
}
console.log(
  solution(
    [1, 5, 2, 6, 3, 7, 4],
    [
      [2, 5, 3],
      [4, 4, 1],
      [1, 7, 3],
    ]
  )
);
