function solution(tickets) {
  const answer = [];

  const DFS = (board, country, choice) => {
    if (board.length === 0) answer.push(choice);
    else {
      for (let i = 0; i < board.length; i++) {
        if (board[i][0] === country) {
          let u = board.slice();
          u.splice(i, 1);
          DFS(u, board[i][1], choice.concat(board[i][1]));
        }
      }
    }
  };
  DFS(tickets, "ICN", ["ICN"]);
  return answer.sort()[0];
}
console.log(
  solution([
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
  ])
);
