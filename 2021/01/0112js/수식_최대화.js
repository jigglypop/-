function solution(expression) {
  let answer = 0;
  const orders = [
    ["*", "+", "-"],
    ["*", "-", "+"],
    ["+", "*", "-"],
    ["+", "-", "*"],
    ["-", "*", "+"],
    ["-", "+", "*"],
  ];
  const calc = {
    "*": (a, b) => {
      return a * b;
    },
    "-": (a, b) => {
      return a - b;
    },
    "+": (a, b) => {
      return a + b;
    },
  };
  let word = expression.match(/[\d]+/g).map(Number);
  let cal = expression.match(/[*|+|-]/g);
  let words = [word[0]];
  for (let i = 0; i < cal.length; i++) {
    words.push(cal[i]);
    words.push(word[i + 1]);
  }
  for (let order of orders) {
    let _words = [...words];
    for (let o of order) {
      let S = [];
      for (let word of _words) {
        if (!S.length) {
          S.push(word);
        } else {
          if (S[S.length - 1] === o) {
            S.push(calc[S.pop()](S.pop(), word));
          } else {
            S.push(word);
          }
        }
      }
      _words = [...S];
      if (_words.length === 1) {
        answer = Math.max(Math.abs(_words[0]), answer);
      }
    }
  }
  return answer;
}
console.log(solution("50*6-3*2"));
