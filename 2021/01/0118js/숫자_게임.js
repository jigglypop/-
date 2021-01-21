function solution(A, B) {
  let answer = 0;
  A = A.sort((a, b) => b - a);
  B = B.sort((a, b) => b - a);
  let j = 0;
  let i = 0;
  let N = A.length;
  while (i < N && j < N) {
    if (B[i] > A[j]) {
      i++;
      answer++;
    }
    j++;
  }
  return answer;
}
console.log(solution([5, 1, 3, 7], [2, 2, 6, 8]));
