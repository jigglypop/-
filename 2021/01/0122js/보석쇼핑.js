function solution(gems) {
  const count = new Set(gems).size;
  const table = new Map();
  const L = [];
  gems.forEach((gem, i) => {
    table.delete(gem);
    table.set(gem, i);
    if (table.size === count) {
      L.push([table.values().next().value + 1, i + 1]);
    }
  });
  L.sort((a, b) => {
    if (a[1] - a[0] === b[1] - b[0]) {
      return a[1] - b[1];
    }
    return a[1] - a[0] - (b[1] - b[0]);
  });
  return L[0];
}
console.log(solution(["A", "A", "B"]));
