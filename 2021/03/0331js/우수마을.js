// const input = require('fs').readFileSync('/dev/stdin').toString().split("\n");
// const input = require('fs').readFileSync('dev/stdin').toString().split('\n').map(x=>x.split(' ').map(x=>x.trim()));

const input = require("fs").readFileSync("./1949.txt").toString().split("\n");
const N = parseInt(input[0]);
const cost = [0, ...input[1].split(" ").map(Number)];
const dp = Array.from(Array(N + 1), () => Array(2).fill(0));
const tree = Array.from(Array(N + 1), () => new Array());
for (let i = 2; i < 2 + N - 1; i++) {
  const [a, b] = input[i].split(" ").map(Number);
  tree[a].push(b);
  tree[b].push(a);
}

const dfs = (prev, u) => {
  dp[u][0] = 0;
  dp[u][1] = cost[u];
  for (let v of tree[u]) {
    if (prev !== v) {
      dfs(u, v);
      dp[u][0] += Math.max(dp[v][0], dp[v][1]);
      dp[u][1] += dp[v][0];
    }
  }
};

dfs(0, 1);
console.log(Math.max(dp[1][0], dp[1][1]));
