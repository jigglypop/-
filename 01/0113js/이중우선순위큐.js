function solution(operations) {
  var Q = [];
  operations = operations.map((x) => x.split(" "));
  for (let operation of operations) {
    if (operation[0] === "I") {
      Q.push(parseInt(operation[1]));
      Q = Q.sort((a, b) => a - b);
    } else {
      if (parseInt(operation[1]) === 1) {
        Q.pop();
        Q = Q.sort((a, b) => a - b);
      } else {
        Q.shift();
        Q = Q.sort((a, b) => a - b);
      }
    }
  }
  if (!Q.length) {
    return [0, 0];
  }
  return [Q.pop(), Q.shift()];
}
console.log(
  solution([
    "I -45",
    "I 653",
    "D 1",
    "I -642",
    "I 45",
    "I 97",
    "D 1",
    "D -1",
    "I 333",
  ])
);
