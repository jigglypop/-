// function solution(arr, divisor) {
//   arr.sort((a, b) => {
//     return a - b;
//   });
//   var answer = [];
//   for (let a of arr) {
//     if (a % divisor === 0) {
//       answer.push(a);
//     }
//   }
//   if (answer.length === 0) {
//     return [-1];
//   }
//   return answer;
// }
function solution(arr, divisor) {
  var answer = arr.filter((x) => x % divisor === 0);
  return answer.length === 0
    ? [-1]
    : answer.sort((a, b) => {
        return a - b;
      });
}
console.log(solution([5, 9, 7, 10], 5));
