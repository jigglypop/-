function solution(answers) {
  var supo1 = "12345".repeat(Math.round(answers.length / 5) + 1);
  var supo2 = "21232425".repeat(Math.round(answers.length / 8) + 1);
  var supo3 = "3311224455".repeat(Math.round(answers.length / 10) + 1);
  var count = [0, 0, 0];

  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === parseInt(supo1.charAt(i))) count[0]++;
    if (answers[i] === parseInt(supo2.charAt(i))) count[1]++;
    if (answers[i] === parseInt(supo3.charAt(i))) count[2]++;
  }
  var count_index = [];
  var _max = Math.max(...count);
  for (let i = 0; i < 3; i++) {
    if (count[i] === _max) {
      count_index.push(i + 1);
    }
  }
  return count_index;
}
console.log(solution([1, 2, 3, 4, 5]));
