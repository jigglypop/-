function solution(n, computers) {
  var answer = 0;
  var check = Array(n).fill(-1);
  var count = 0;
  const DFS = (x) => {
    var S = [0];
    check[x] = count;
  };
  return answer;
}
console.log(
  solution(3, [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
  ])
);
