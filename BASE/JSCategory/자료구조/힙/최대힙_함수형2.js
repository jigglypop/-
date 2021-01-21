var heap = [0];

const swap = (a, b) => {
  [heap[a], heap[b]] = [heap[b], heap[a]];
};

const heappush = (v) => {
  heap.push(v);
  let i = heap.length - 1;
  while (i > 1 && heap[Math.floor(i / 2)] < heap[i]) {
    swap(i, Math.floor(i / 2));
    i = Math.floor(i / 2);
  }
};

const heappop = () => {
  if (heap.length <= 1) return 0;
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
for (let i = 1; i < 10; i++) {
  heappush(i);
}
for (let i = 1; i < 10; i++) {
  console.log(heappop());
}
