function solution(words) {
  let answer = 0;
  let count = 0;
  while (true) {
    words = words.split("");
    let temp = words.filter((word) => word === "0").length;
    words = words.filter((word) => word === "1").length.toString(2);
    answer += temp;
    count++;
    if (words === "1") break;
  }
  return [count, answer];
}
console.log(solution("110010101001"));
