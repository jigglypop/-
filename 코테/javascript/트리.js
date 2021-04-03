// 트리 순회

// class Node {
//   constructor(value, left, right) {
//     this.value = value;
//     this.left = left;
//     this.right = right;
//   }
// }

// const preorder = (x) => {
//   if (x === -19) return;
//   process.stdout.write(makeString(x));
//   preorder(tree[x].left);
//   preorder(tree[x].right);
// };

// const inorder = (x) => {
//   if (x === -19) return;
//   inorder(tree[x].left);
//   process.stdout.write(makeString(x));
//   inorder(tree[x].right);
// };

// const postorder = (x) => {
//   if (x === -19) return;
//   postorder(tree[x].left);
//   postorder(tree[x].right);
//   process.stdout.write(makeString(x));
// };

// var fs = require("fs");
// // const input = fs.readFileSync('dev/stdin').toString().split('\n');
// var input = fs.readFileSync("./1991.txt").toString().split("\r\n");

// const makeNumber = (x) => {
//   return x.charCodeAt(0) - 65;
// };
// const makeString = (x) => {
//   return String.fromCharCode(x + 65);
// };
// const N = parseInt(input[0]);
// input.shift();
// const tree = new Array(26);
// for (let i = 0; i < N; i++) {
//   const [A, B, C] = input[i].split(" ").map((x) => makeNumber(x));
//   tree[A] = new Node(A, B, C);
// }

// preorder(0);
// process.stdout.write("\n");
// inorder(0);
// process.stdout.write("\n");
// postorder(0);
// process.stdout.write("\n");

// 크루스칼

// var idx = 0;
// const V = parseInt(input[idx++]);
// const E = parseInt(input[idx++]);

// var parent = new Array(V + 1).fill(0).map((_, i) => i);
// var edges = [];
// for (let i = 0; i < E; i++) {
//   [a, b, cost] = input[idx++].split(" ").map(Number);
//   edges.push([cost, a, b]);
// }
// edges.sort((a, b) => a[0] - b[0]);
// let result = 0;
// const find = (x) => {
//   if (parent[x] === x) return x;
//   return (parent[x] = find(parent[x]));
// };

// const union = (_a, _b) => {
//   var a = find(_a);
//   var b = find(_b);
//   parent[a] = b;
// };

// for (let [cost, a, b] of edges) {
//   if (find(a) !== find(b)) {
//     union(a, b);
//     result += cost;
//   }
// }
// console.log(result);

// DAG

// const [N, M] = input[0].split(" ").map(Number);
// const tree = Array.from(Array(N + 1), () => Array());
// const check = Array(N + 1).fill(0);

// for (let i = 1; i < M + 1; i++) {
//   const [a, b] = input[i].split(" ").map(Number);
//   tree[a].push(b);
//   check[b]++;
// }

// const Q = [];
// for (let i = 1; i < N + 1; i++) {
//   if (check[i] === 0) Q.push(i);
// }
// const result = [];
// while (Q.length) {
//   let u = Q.shift();
//   resultA.push(u);
//   for (let v of tree[u]) {
//     check[v]--;
//     if (check[v] === 0) {
//       Q.push(v);
//     }
//   }
//   result.push(u);
// }
// console.log(result.join(" "));

function solution(num) {
  return fibo(num);
}
console.log(solution(3));
