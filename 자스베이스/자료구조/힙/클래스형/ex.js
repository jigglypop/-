// const data = require("fs")
//   .readFileSync("/dev/stdin", "utf8")
//   .toString()
//   .trim()
//   .split("\n");
const input = require("fs")
  .readFileSync("./11279.txt", "utf8")
  .toString()
  .split("\n")
  .map(Number);

class Heap {
  N = input[0];
  heap = [0];

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }
  push(v) {
    this.heap.push(v);
    let i = this.heap.length - 1;
    while (i > 1 && this.heap[Math.floor(i / 2) < this.heap[i]]) {
      this.swap(i, Math.floor(i / 2));
      i = Math.floor(i / 2);
    }
  }

  pop() {
    if (this.heap.length <= 1) {
      return 0;
    }
    let x = this.heap[1];
    this.heap[1] = this.heap[heap.length - 1];
    this.heap.pop();
    let i = 1;
    while (i * 2 < this.heap.length) {
      let max = this.heap[i * 2];
      let _i = i * 2;
      if (i * 2 + 1 < this.heap.length && max < this.heap[i * 2 + 1]) {
        max = this.heap[i * 2 + 1];
        _i = i * 2 + 1;
      }
      if (this.heap[i] > max) break;
      this.swap(i, _i);
      i = _i;
    }
    return x;
  }
}

let answer = "";
let heap = new Heap();
for (let i = 1; i <= input[0]; i++) {
  if (input[i] === 0) {
    answer += heap.pop() + "\n";
  } else {
    heap.push(input[i]);
  }
}
console.log(answer);
