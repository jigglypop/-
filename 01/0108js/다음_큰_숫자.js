function solution(n) {
  let count = n.toString(2).match(/1/g).length;
  for (let i = n + 1; i <= 1000000; i++) {
    if (i.toString(2).match(/1/g).length === count) {
      return i;
    }
  }
}
console.log(solution(15));
