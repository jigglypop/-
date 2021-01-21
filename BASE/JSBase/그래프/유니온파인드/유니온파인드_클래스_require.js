// const input = require("fs").readFileSync("/dev/stdin", "utf8").toString().trim().split("\r\n").map((x) => x.split(" ").map(Number));
const input = require("fs")
  .readFileSync("./1717.txt")
  .toString()
  .split("\r\n")
  .map((x) => x.split(" ").map((x) => parseInt(x)));

class Tree {
  constructor(n) {
    this.parent = Array(n + 1)
      .fill(0)
      .map((_, i) => i);
  }

  union(n1, n2) {
    const a = this.find(n1);
    const b = this.find(n2);
    this.parent[b] = a;
  }

  find(node) {
    if (this.parent[node] === node) {
      return node;
    }
    this.parent[node] = this.find(this.parent[node]);
    return this.parent[node];
  }
}
const solve = () => {
  const [n, m] = input[0];
  input.shift();
  const tree = new Tree(n);
  let answer = "";
  for (let i = 0; i < m; ++i) {
    const [a, b, c] = input[i];
    if (a === 0) {
      tree.union(b, c);
    } else {
      if (tree.find(b) === tree.find(c)) {
        answer += "YES\n";
      } else {
        answer += "NO\n";
      }
    }
  }
  console.log(answer);
};
solve();
