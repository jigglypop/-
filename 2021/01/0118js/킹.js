// var input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n")
var input = require("fs")
  .readFileSync("./1063.txt")
  .toString()
  .trim()
  .split("\r\n");

let nums = input[0].split(" ");
let king = nums[0].split("");
let stone = nums[1].split("");
king[0] = king[0].charCodeAt(0) - 65;
stone[0] = stone[0].charCodeAt(0) - 65;
king[1] = 8 - parseInt(king[1]);
stone[1] = 8 - parseInt(stone[1]);
king = king.reverse();
stone = stone.reverse();

let table = {
  R: [0, 1],
  L: [0, -1],
  B: [1, 0],
  T: [-1, 0],
  RT: [-1, 1],
  LT: [-1, -1],
  RB: [1, 1],
  LB: [1, -1],
};
for (let i = 1; i < parseInt(nums[2]) + 1; i++) {
  let [y, x] = king;
  let [dy, dx] = table[input[i]];
  let [ny, nx] = [y + dy, x + dx];
  if (0 <= ny && ny < 8 && 0 <= nx && nx < 8) {
    let [sy, sx] = stone;
    if (sy === ny && sx === nx) {
      let [sny, snx] = [sy + dy, sx + dx];
      if (0 <= sny && sny < 8 && 0 <= snx && snx < 8) {
        king = [ny, nx];
        stone = [sny, snx];
      }
    } else {
      king = [ny, nx];
    }
  }
}
king = king.reverse();
stone = stone.reverse();
king[0] = String.fromCharCode(king[0] + 65);
stone[0] = String.fromCharCode(stone[0] + 65);
king[1] = 8 - king[1];
stone[1] = 8 - stone[1];
console.log(king.join(""));
console.log(stone.join(""));
