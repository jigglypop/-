const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
// const input = require("fs")
//   .readFileSync("./1213.txt")
//   .toString()
//   .trim()
//   .split("\n");
var a = [];
var c = 0;
while (c <= 1 && s.length > 1) {
  var t = s.shift();
  var k = s.indexOf(t);
  if (k === -1) {
    ++c;
    s.push(t);
  } else {
    a.push(t);
    s.splice(k, 1);
  }
}
if (s.length > 1) {
  console.log("I'm Sorry Hansoo");
} else {
  a = a.sort(function (x, y) {
    return x.charCodeAt() - y.charCodeAt();
  });
  var x = a.join("");
  if (s.length === 1) {
    x += s[0];
  }
  x += a.reverse().join("");
  console.log(x);
}
