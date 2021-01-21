function solution(n, results) {
  let answer = 0;
  var treeA = Array.from(Array(n), () => Array());
  var treeB = Array.from(Array(n), () => Array());

  for (let result of results) {
    let a = --result[0];
    let b = --result[1];
    treeA[a].push(b);
    treeB[b].push(a);
  }
  const BFS = (start, tree) => {
    let check = Array(n).fill(false);
    let Q = [start];
    check[start] = true;
    while (Q.length) {
      let u = Q.shift();
      for (let v of tree[u]) {
        if (!check[v]) {
          check[v] = true;
          Q.push(v);
        }
      }
    }
    return check;
  };
  for (let i = 0; i < n; i++) {
    let checkA = BFS(i, treeA);
    let checkB = BFS(i, treeB);
    let flag = true;
    for (let i = 0; i < n; i++) {
      if (!checkA[i] && !checkB[i]) flag = false;
    }
    if (flag) answer++;
  }
  return answer;
}
console.log(
  solution(5, [
    [4, 3],
    [4, 2],
    [3, 2],
    [1, 2],
    [2, 5],
  ])
);
