// const input = require('fs').readFileSync('/dev/stdin').toString();
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

var input = require("fs").readFileSync("./10451.txt").toString().split("\n");

var testCase = Number(input[0]);
var check, graph;
var DFS = (index) => {
  check[index] = true;
  for (var i = 0; i < graph[index].length; i++) {
    var next = graph[index][i];
    if (check[next] === false) {
      DFS(next);
    }
  }
};
for (var i = 1; i <= testCase; i++) {
  var result = 0;
  var graph = [];
  var check = [];
  var V = Number(input[2 * i - 1]);
  var vertexInfo = input[2 * i].split(" ").map(Number);

  for (var j = 0; j <= V; j++) {
    check[j] = false;
    graph[j] = [];
  }
  for (var j = 0; j < vertexInfo.length; j++) {
    graph[j + 1].push(vertexInfo[j]);
    graph[vertexInfo[j]].push(j + 1);
  }
  for (var j = 1; j <= V; j++) {
    if (check[j] === false) {
      result++;
      DFS(j);
    }
  }
  console.log(result);
}
