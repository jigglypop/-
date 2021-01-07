// function solution(numbers) {
//   let N = numbers.length;
//   var Max = 0;
//   const perm = (k, used, choice) => {
//     if (k === N) {
//       Max = Math.max(parseInt(choice.join("")), Max);
//       return;
//     }
//     for (let i = 0; i < N; i++) {
//       if (used & (1 << i)) continue;
//       choice.push(numbers[i]);
//       perm(k + 1, used | (1 << i), choice);
//       choice.pop();
//     }
//   };
//   perm(0, 0, []);
//   return Max;
// }
function solution(numbers) {
  let result = numbers
    .map(String)
    .sort((a, b) => b + a - (a + b))
    .join("");
  return result[0] === "0" ? "0" : result;
}
console.log(solution([3, 30, 34, 5, 9]));
