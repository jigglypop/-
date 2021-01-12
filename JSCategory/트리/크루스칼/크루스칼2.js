var fs = require("fs");
// var input = fs.readFileSync("/dev/stdin", "utf8").split("\n");
var input = fs.readFileSync("./1922.txt", "utf8").split("\r\n");
var idx = 0;
var V = parseInt(parseInt(input[idx++]));
var E = parseInt(parseInt(input[idx++]));
var parent = new Array(V + 1).fill(-1);

const find = (n) => {
  if (parent[n] < 0) return n;
  return (parent[n] = find(parent[n]));
};

const union = (_a, _b) => {
  var a = find(_a);
  var b = find(_b);
  parent[a] = b;
};
var edges = [];
for (var i = 0; i < E; i++) {
  var tmp = input[idx++].split(" ").map(Number);
  edges.push({
    from: tmp[0],
    to: tmp[1],
    cost: tmp[2],
  });
}

edges.sort((a, b) => b.cost - a.cost);
var result = 0;
while (edges.length) {
  var edge = edges.pop();
  if (find(edge.from) !== find(edge.to)) {
    result += edge.cost;
    union(edge.from, edge.to);
  }
}
console.log(result);
