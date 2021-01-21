// function solution(n) {
//   var result = [];
//   for (let i = 0; i < n; i++) {
//     if (i % 2 === 0) {
//       result.push("수");
//     } else {
//       result.push("박");
//     }
//   }
//   return result.join("");
// }
function solution(n) {
  return "수박".repeat(n / 2) + (n % 2 !== 0 ? "수" : "");
}
console.log(solution(9));
