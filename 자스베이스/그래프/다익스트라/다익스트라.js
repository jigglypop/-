var input = require("fs")
    .readFileSync("./dev/stdin")
    .toString()
    .trim()
    .split("\n");

// const input = require("fs").readFileSync("./1916.txt").toString().split("\r\n");

class MinHeap {
    heap = [0];

    swap(a, b) {
        [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
    }
    push(v) {
        this.heap.push(v);
        let i = this.heap.length - 1;
        while (i > 1 && this.heap[Math.floor(i / 2)] > this.heap[i]) {
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
            if (i * 2 + 1 < this.heap.length && max > this.heap[i * 2 + 1]) {
                max = this.heap[i * 2 + 1];
                _i = i * 2 + 1;
            }
            if (this.heap[i] < max) break;
            this.swap(i, _i);
            i = _i;
        }
        return x;
    }
}

const N = parseInt(input[0]);
const M = parseInt(input[1]);

const INF = Infinity;
const dist = Array(N + 1).fill(INF);
const graph = Array.from(Array(N + 1), () => Array());

for (let i = 2; i < M + 2; i++) {
    const [a, b, c] = input[i].split(" ").map(Number);
    graph[a].push([c, b]);
}
const [A, B] = input[M + 2].split(" ").map(Number);

const heap = new MinHeap();
heap.push([0, A]);
dist[A] = 0;
while (heap.heap.length > 1) {
    let [cost, u] = heap.pop();
    if (dist[u] < cost) continue;
    for (let [w, v] of graph[u]) {
        if (dist[v] > dist[u] + w) {
            dist[v] = dist[u] + w;
            heap.push([dist[v], v]);
        }
    }
}
console.log(dist[B]);
