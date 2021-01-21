// var input = require("fs").readFileSync("./dev/stdin").toString().split("\n");
var input = require("fs").readFileSync("./2304.txt").toString().split("\n");

let result = 0;
input.shift();
let stroage = new Array(1001).fill(0);
input = input.map((e) => e.split(" ").map((e) => +e));
input.sort((a, b) => a[0] - b[0]);

let S = [];
let Max = input.reduce(
  (pre, cur) => {
    return pre[1] <= cur[1] ? cur : pre;
  },
  [0, 0]
);

result += Max[1];
input.forEach((e) => (stroage[e[0]] = e[1]));
let start = 0;
S.push(0);
for (let i = start; i < Max[0]; i++) {
  if (S[S.length - 1] < stroage[i]) {
    S.pop();
    S.push(stroage[i]);
  }
  result += S[S.length - 1];
}

S = [];
S.push(0);
for (let i = input[input.length - 1][0]; i > Max[0]; i--) {
  if (S[S.length - 1] < stroage[i]) {
    S.pop();
    S.push(stroage[i]);
  }
  result += S[S.length - 1];
}
console.log(result);
