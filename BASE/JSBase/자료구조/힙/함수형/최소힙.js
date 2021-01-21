class Heap {
  constructor() {
    this.heap = [0];
  }
  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }
  push(value) {
    this.heap.push(value);
    let idx = this.heap.length - 1;
    while (idx > 1 && this.heap[Math.floor(idx / 2)] < this.heap[idx]) {
      this.swap(idx, Math.floor(idx / 2));
      idx = Math.floor(idx / 2);
    }
  }
  pop() {
    if (this.heap.length < 2) return 0;
    let value = this.heap[1];
    this.heap[1] = this.heap[this.heap.length - 1];
    this.heap.pop();
    let idx = 1;
    while (idx * 2 < this.heap.length) {
      let max_value = this.heap[idx * 2];
      let max_idx = idx * 2;
      if (
        idx * 2 + 1 < this.heap.length &&
        max_value < this.heap[idx * 2 + 1]
      ) {
        max_value = this.heap[idx * 2 + 1];
        max_idx = idx * 2 + 1;
      }
      if (this.heap[idx] > max_value) break;
      this.swap(idx, max_idx);
      idx = max_idx;
    }
    return value;
  }
}

const heap = new Heap();
for (let i = 1; i < 10; i++) {
  heap.push(i);
}
console.log(heap.heap);
// for (let i = 1; i < 10; i++) {
//   console.log(heap.pop());
// }
