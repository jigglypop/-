const isDifferentOne = (A, B) => {
  let count = 0;
  for (let i = 0; i < A.length; i++) {
    if (A[i] !== B[i]) count++;
  }
  if (count === 1) {
    return true;
  } else {
    return false;
  }
};
function solution(begin, target, words) {
  var answer = 0;

  if (words.includes(begin)) {
    words.splice(words.indexOf(begin), 1);
  }
  if (words.includes(target)) {
    words.splice(words.indexOf(target), 1);
  } else {
    return 0;
  }
  words = [begin, ...words, target];
  let tree = Array.from(Array(words.length), () => Array());
  for (let i = 0; i < words.length; i++) {
    for (let j = 0; j < words.length; j++) {
      if (isDifferentOne(words[i], words[j])) {
        tree[i].push(j);
      }
    }
  }
  let S = [];
  let check = Array(words.length).fill(-1);
  let start = 0;
  let finish = words.length - 1;
  check[start] = 0;
  S.push(0);
  while (S.length) {
    let u = S.pop();
    if (u === finish) {
      answer = check[u];
      break;
    }
    for (let v of tree[u]) {
      if (check[v] === -1) {
        check[v] = check[u] + 1;
        S.push(v);
      }
    }
  }
  return answer;
}
console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]));
