function solution(n, computers) {
  var check = Array(n).fill(-1);
  var count = 0;
  const DFS = (x) => {
    let S = [x];
    check[x] = count;
    while (S.length) {
      let s = S.pop();
      for (let i = 0; i < computers[s].length; i++) {
        if (computers[s][i] === 1 && check[i] === -1) {
          S.push(i);
          check[i] = count;
        }
      }
    }
  };
  for (let i = 0; i < n; i++) {
    if (check[i] === -1) {
      count++;
      DFS(i);
    }
  }
  return count;
}
console.log(
  solution(3, [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
  ])
);
