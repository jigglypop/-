// function solution(arr1, arr2) {
//   for (let y = 0; y < arr1.length; y++) {
//     for (let x = 0; x < arr1[y].length; x++) {
//       arr1[y][x] += arr2[y][x];
//     }
//   }
//   return arr1;
// }
function solution(A, B) {
  return A.map((a, y) => a.map((b, x) => (b += B[y][x])));
}
console.log(
  solution(
    [
      [1, 2],
      [2, 3],
    ],
    [
      [3, 4],
      [5, 6],
    ]
  )
);
