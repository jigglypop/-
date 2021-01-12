const input = require("fs")
  .readFileSync("./11279.txt", "utf8")
  .toString()
  .split("\n")
  .map(Number);

const N = input[0];
var heap = [0];

const swap = (a, b) => {
  [heap[a], heap[b]] = [heap[b], heap[a]];
};

const heappush = (v) => {
  heap.push(v);
  let i = heap.length - 1;
  while (i > 1 && heap[Math.floor(i / 2)] < heap[i]) {
    swap(Math.floor(i / 2), i);
    i = Math.floor(i / 2);
  }
};

const heappop = () => {
  if (heap.length < 2) return 0;
  let x = heap[1];
  heap[1] = heap[heap.length - 1];
  heap.pop();
  let i = 1;
  while (i * 2 < heap.length) {
    let _i = [i * 2, i * 2 + 1].reduce(
      (_i, i) => (heap[_i] < heap[i] ? i : _i),
      i * 2
    );
    if (heap[i] > heap[_i]) break;
    swap(i, _i);
    i = _i;
  }
  return x;
};
let answer = "";
for (let i = 1; i <= N; i++) {
  if (input[i] === 0) {
    answer += heappop() + "\n";
  } else {
    heappush(input[i]);
  }
}
console.log(answer);
