// const heap = [100, 101, 102];
const heap = [105, 103, 101, 102];
// undefined 가 아니거나 heap[_i] < heap[i] 일 때 i, 아니면 _i
const Max = [2, 1, 5, 3].reduce((_i, i) => (heap[_i] < heap[i] ? i : _i), 2);
console.log(Max);
// let [[_i, max]] = [1, 3]
//   .filter((x) => x < heap.length)
//   .map((x) => [heap[x], x])
//   .sort((a, b) => b[0] - a[0]);
// console.log(_i, max);
