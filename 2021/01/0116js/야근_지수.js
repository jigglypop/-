class MaxHeap {
  heap = [0];

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }
  push(v) {
    this.heap.push(v);
    let i = this.heap.length - 1;
    while (i > 1 && this.heap[Math.floor(i / 2)] < this.heap[i]) {
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

function solution(n, works) {
  let maxHeap = new MaxHeap();
  for (let work of works) {
    maxHeap.push(work);
  }
  while (n > 0 && maxHeap.heap.length >= 1) {
    n--;
    let mh = maxHeap.pop();
    if (mh - 1 <= 0) continue;
    mh -= 1;
    maxHeap.push(mh);
  }
  var answer = 0;
  while (maxHeap.heap.length > 1) {
    answer += maxHeap.pop() ** 2;
  }
  return answer;
}
console.log(solution(1, [2, 1, 2]));
