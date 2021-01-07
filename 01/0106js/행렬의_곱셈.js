function solution(A, B) {
  let Y = A.length;
  let X = B[0].length;
  let Z = A[0].length;
  var answer = Array.from(Array(Y), () => Array(X).fill(0));
  for (let y = 0; y < Y; y++) {
    for (let x = 0; x < X; x++) {
      for (let z = 0; z < Z; z++) {
        answer[y][x] += A[y][z] * B[z][x];
      }
    }
  }
  return answer;
}

console.log(
  solution(
    [
      [1, 4],
      [3, 2],
      [4, 1],
    ],
    [
      [3, 3],
      [3, 3],
    ]
  )
);
