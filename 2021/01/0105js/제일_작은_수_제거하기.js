function solution(arr) {
  return arr.length === 1 ? [-1] : arr.filter((x) => x !== Math.min(...arr));
}
console.log(solution([4, 3, 2, 1]));
