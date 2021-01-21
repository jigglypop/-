function solution(words) {
  return words
    .split(" ")
    .map((x) => x.toLowerCase())
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1, word.length))
    .join(" ");
}
console.log(solution("3people unFollowed me"));
