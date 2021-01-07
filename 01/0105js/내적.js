// function solution(a, b) {
//   var answer = 0;
//   for (let i = 0; i < a.length; i++) {
//     answer += a[i] * b[i];
//   }
//   return answer;
// }
function solution(A, B) {
  return A.reduce((result, a, i) => (result += a * B[i]), 0);
}
// 배열.reduce((누적값, 현잿값, 인덱스, 요소) => { return 결과 }, 초깃값);
console.log(solution([1, 2, 3, 4], [-3, -1, 0, 2]));
