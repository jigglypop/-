function solution(n, weak, dist) {
  dist.sort((a, b) => b - a);

  for (let i = 0; i < dist.length; i++) {
    for (let j = 0; j < weak.length; j++) {
      let tempWeak = weak.map(
        (_, c) => weak[(j + c) % weak.length] + (j + c >= weak.length ? n : 0)
      );
      let tempDist = dist.slice(0, i + 1);

      for (let k = 0; k <= i; k++) {
        const range = tempWeak[0] + tempDist[0];
        let rangeIn = 0;

        for (let m = 0; m < tempWeak.length; m++) {
          if (tempWeak[m] <= range) {
            rangeIn++;
          } else {
            break;
          }
        }
        for (let n = tempDist.length - 1; n >= 0; n--) {
          if (tempWeak[rangeIn - 1] - tempWeak[0] <= tempDist[n] && n !== 0) {
            tempDist.splice(n, 1);
            break;
          } else if (n === 0) {
            tempDist.shift();
          }
        }
        tempWeak.splice(0, rangeIn);

        if (tempWeak.length === 0) {
          return i + 1;
        }
      }
    }
  }

  return -1;
}
console.log(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]));
