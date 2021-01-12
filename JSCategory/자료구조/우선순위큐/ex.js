const data = require("fs")
  .readFileSync("/dev/stdin", "utf8")
  .toString()
  .trim()
  .split("\n");
// const input = require("fs").readFileSync("./11279.txt").split("\n").map(Number);

const N = Number(data[0]);
data.shift();
const input = data.map(Number);
const heap = [0];

const swap = (a, b) => {
  let temp = a;
  a = b;
  b = temp;
};

const heappush = (v) => {
  heap.push(v);
  let p = heap.length - 1;
  while (p > 1 && heap[Math.floor(p / 2)] < heap[p]) {
    swap(heap[Math.floor(p / 2)], heap[p]);
    p = Math.floor(p / 2);
  }
};

const heappop = () => {
  if (heap.length - 1 < 1) {
    return 0;
  }
  let deletedItem = heap[1];

  heap[1] = heap[heap.length - 1];
  heap.pop();

  let p = 1;
  while (p * 2 < heap.length) {
    let max = heap[p * 2];
    let maxP = p * 2;
    if (p * 2 + 1 < heap.length && max < heap[p * 2 + 1]) {
      max = heap[p * 2 + 1];
      maxP = p * 2 + 1;
    }
    if (heap[p] > max) {
      break;
    }
    swap(heap[p], heap[maxP]);
    p = maxP;
  }
  return deletedItem;
};
let answer = "";
for (let i = 0; i < N; i++) {
  if (input[i] === 0) {
    answer += heappop() + "\n";
  } else {
    heappush(input[i]);
  }
}
console.log(answer);
