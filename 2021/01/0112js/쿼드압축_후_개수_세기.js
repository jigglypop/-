function solution(arr) {
  var answer = [0, 0];
  let Y = arr.length;
  let X = arr[0].length;
  const go = (sy, sx, ey, ex) => {
    let N = (ex - sx) / 2;
    let start = arr[sy][sx];
    let flag = true;
    for (let y = sy; y < ey; y++) {
      for (let x = sx; x < ex; x++) {
        if (start !== arr[y][x]) flag = false;
      }
    }
    if (flag === true) {
      answer[start]++;
      return;
    }
    go(sy, sx, sy + N, sx + N);
    go(sy + N, sx, ey, sx + N);
    go(sy, sx + N, sy + N, ex);
    go(sy + N, sx + N, ey, ex);
  };
  go(0, 0, Y, X);
  return answer;
}
console.log(
  solution([
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 1, 1],
  ])
);
