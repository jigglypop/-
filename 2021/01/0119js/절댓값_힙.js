// var input = require("fs").readFileSync("./dev/stdin").toString().split("\n");
var input = require("fs").readFileSync("./11286.txt").toString().split("\n");
class MinHeap {
  heap = [0];
  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }
  push(v) {
    this.heap.push(v);
    let i = this.heap.length - 1;
    while (
      i > 1 &&
      Math.abs(this.heap[Math.floor(i / 2)]) > Math.abs(this.heap[i])
    ) {
      this.swap(i, Math.floor(i / 2));
      i = Math.floor(i / 2);
    }
  }
  pop() {
    if (this.heap.length <= 1) return 0;
    let x = this.heap[1];
    this.heap[1] = this.heap[this.heap.length - 1];
    this.heap.pop();
    let i = 1;
    while (i * 2 < this.heap.length) {
      let max = Math.abs(this.heap[i * 2]);
      let _i = i * 2;
      if (
        i * 2 + 1 < this.heap.length &&
        max > Math.abs(this.heap[i * 2 + 1])
      ) {
        max = this.heap[i * 2 + 1];
        _i = i * 2 + 1;
      }
      if (Math.abs(this.heap[i]) < Math.abs(max)) break;
      this.swap(i, _i);
      i = _i;
    }
    return x;
  }
}
const N = parseInt(input[0]);
let heap = new MinHeap();
for (let i = 1; i < N + 1; i++) {
  let num = parseInt(input[i]);
  if (num === 0) {
    console.log(heap.pop());
  } else {
    heap.push(num);
  }
}
