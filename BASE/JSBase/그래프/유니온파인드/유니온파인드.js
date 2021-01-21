const input = require("fs")
  .readFileSync("./1717.txt")
  .toString()
  .split("\r\n")
  .map((x) => x.split(" ").map(Number));
// const input = require("fs").readFileSync("/dev/stdin", "utf8").toString().trim().split("\n").map((x) => x.split(" ").map(Number));
const [n, m] = input[0];
input.shift();
parent = Array(n + 1)
  .fill(0)
  .map((_, i) => i);

function find(x) {
  if (parent[x] === x) {
    return x;
  } else {
    let temp = find(parent[x]);
    parent[x] = temp;
    return temp;
  }
}

function union(a, b) {
  a = find(a);
  b = find(b);
  if (a !== b) {
    parent[b] = a;
  }
}

for (let i = 0; i < input.length; i++) {
  const [a, b, c] = input[i];
  if (a === 0) {
    union(b, c);
  } else {
    if (find(b) === find(c)) {
      console.log("YES");
    } else {
      console.log("NO");
    }
  }
}
