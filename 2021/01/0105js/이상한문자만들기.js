// function solution(s) {
//   return s.split("").reduce((result, word, i) => {
//     result +=
//       word === " "
//         ? " "
//         : word === word.toUpperCase()
//         ? word.toUpperCase()
//         : word.toLowerCase();
//   }, 0);
// }
function solution(s) {
  return s
    .split(" ")
    .map((word) =>
      word
        .split("")
        .map((w, idx) => (idx % 2 === 1 ? w.toLowerCase() : w.toUpperCase()))
        .join("")
    )
    .join(" ");
}
console.log(solution("try hello world"));
