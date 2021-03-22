const Input = require("fs")
  .readFileSync("./1717.txt")
  .toString()
  .split("\r\n")
  .map((x) => x.split(" ").map(Number));

// const input = require("fs").readFileSync("/dev/stdin", "utf8").toString().trim().split("\n").map((x) => x.split(" ").map(Number));
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let Input = [];
let N, M;
let Parent = Array(N + 1)
  .fill(0)
  .map((_, i) => i);
rl.on("line", function (value) {
  value = value.split(" ").map((element) => parseInt(element));
  Input.push(value);
});

rl.on("close", function () {
  [N, M] = Input.shift();
  Solve();
  process.exit();
});

function Find(x) {
  if (Parent[x] == x) {
    return x;
  } else {
    let p = Find(Parent[x]);
    Parent[x] = p;
    return p;
  }
}

function Union(x, y) {
  x = Find(x);
  y = Find(y);
  if (x != y) {
    Parent[y] = x;
  }
}

function Solve() {
  for (let i = 0; i < Input.length; ++i) {
    let x, y;
    x = Input[i][1];
    y = Input[i][2];

    if (Input[i][0] == 0) {
      Union(x, y);
    } else if (Input[i][0] == 1) {
      if (Find(x) == Find(y)) {
        console.log("YES");
      } else {
        console.log("NO");
      }
    }
  }
}
